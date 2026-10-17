"""Grade one iteration of job-mapping-interview eval runs.

Usage: python evals/grade.py <workspace>/iteration-N
Writes grading.json (fields: text, passed, evidence) next to each run's outputs/.
"""
import json
import re
import sys
from pathlib import Path


def assistant_turns(transcript: str) -> list[str]:
    parts = re.split(r"^## (User|Assistant)\s*$", transcript, flags=re.M)
    return [parts[i + 1] for i in range(1, len(parts) - 1, 2) if parts[i] == "Assistant"]


def has_all(text: str, *patterns: str) -> bool:
    return all(re.search(p, text, re.I) for p in patterns)


def common_checks(final: str, turns: list[str]) -> list[tuple[str, bool, str]]:
    headings = [h for h in ("Input", "Do", "Output", "Human Check")
                if re.search(rf"^#+\s*{h}\b", final, re.M | re.I)]
    return [
        ("Map has Input/Do/Output/Human Check headings", len(headings) == 4, f"found {headings}"),
        ("Map has a Test Log section", bool(re.search(r"test log", final, re.I)), ""),
    ]


def interview_checks(turns: list[str]) -> list[tuple[str, bool, str]]:
    # ponytail: '?' count is a proxy for "one question at a time"; ≤2 allows a recap + question
    counts = [t.count("?") for t in turns[:-1]]
    tested = bool(re.search(r"fresh chat|new chat|project", turns[-1] if turns else "", re.I))
    asks_failure = any(re.search(r"(get|getting|got|go|goes|going) wrong", t, re.I) and "?" in t for t in turns[:3])
    return [
        ("At most one question per turn (<=2 '?')", all(c <= 2 for c in counts), f"'?' per turn: {counts}"),
        ("Hand-off tells user to test in fresh chat/Project", tested, ""),
        ("Asks what the AI gets wrong within first 3 turns", asks_failure, ""),
        ("Interview stays under 17 assistant turns", len(turns) <= 16, f"{len(turns)} turns"),
    ]


FACT_CHECKS = {
    "friday-kpi-report": [
        ("Captures test-account filter", [r"acme-test|test account"]),
        ("Captures 15% MQL-drop rule", [r"15\s?%"]),
        ("Captures 9am reclassification cutoff", [r"9\s?(:00)?\s?am"]),
        ("Captures CAC >25% sanity check", [r"25\s?%"]),
        ("Captures dedupe-by-email rule", [r"dedup"]),
    ],
    "vague-whole-role": [
        ("Narrowed to invoice reconciliation", [r"reconcil"]),
        ("Captures consent rule for screen fails", [r"consent"]),
        ("Captures PI sign-off for unscheduled visits", [r"\bPI\b"]),
        ("Captures 10% holdback", [r"10\s?%|holdback"]),
        ("Captures $2,000 manager review", [r"2,?000"]),
    ],
    "patch-existing-sop": [
        ("Names Availity eligibility check", [r"availity"]),
        ("Captures out-of-network self-pay handling", [r"\$?120"]),
        ("Captures portal-down fallback", [r"pending"]),
    ],
}


def grade_run(eval_name: str, outputs: Path) -> list[dict]:
    final = (outputs / "final_output.md").read_text()
    turns = assistant_turns((outputs / "transcript.md").read_text())
    checks = common_checks(final, turns)
    if eval_name == "patch-existing-sop":
        elig, book = final.lower().find("eligib"), final.lower().find("book first")
        checks.append(("Eligibility step placed before booking", elig != -1 and (book == -1 or elig < book), f"eligib@{elig} book@{book}"))
        checks.append(("Quick patch: <=5 assistant turns (incl. confirm)", len(turns) <= 5, f"{len(turns)} turns"))
        confirmed = any(re.search(r"match|right\?|correct\?|look good|accurate", t, re.I) for t in turns[:-1])
        checks.append(("Confirms the patch with the user before final", confirmed, ""))
    else:
        checks += interview_checks(turns)
    for text, patterns in FACT_CHECKS[eval_name]:
        checks.append((text, has_all(final, *patterns), ""))
    return [{"text": t, "passed": p, "evidence": e} for t, p, e in checks]


def main() -> None:
    iteration = Path(sys.argv[1])
    # layout: eval-<id>-<name>/<config>/run-<n>/outputs (what aggregate_benchmark expects)
    for outputs in sorted(iteration.glob("eval-*/*/run-*/outputs")):
        eval_name, config = outputs.parts[-4].split("-", 2)[2], outputs.parts[-3]
        expectations = grade_run(eval_name, outputs)
        passed = sum(e["passed"] for e in expectations)
        summary = {"passed": passed, "failed": len(expectations) - passed, "total": len(expectations),
                   "pass_rate": round(passed / len(expectations), 2)}
        (outputs.parent / "grading.json").write_text(json.dumps({"expectations": expectations, "summary": summary}, indent=2))
        print(f"{eval_name:22} {config:14} {passed}/{len(expectations)}")


if __name__ == "__main__":
    main()
