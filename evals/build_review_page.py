"""Build a one-scenario-at-a-time review page for an eval iteration.

Usage: python evals/build_review_page.py <workspace>/iteration-N
Writes <workspace>/iteration-N/review.html (self-contained; open it in a browser).
"""
import json
import re
import sys
from pathlib import Path

EVALS_DIR = Path(__file__).parent


def parse_transcript(text: str) -> list[dict]:
    parts = re.split(r"^## (User|Assistant)\s*$", text, flags=re.M)
    return [{"role": parts[i].lower(), "text": parts[i + 1].strip()} for i in range(1, len(parts) - 1, 2)]


def load_run(run_dir: Path) -> dict:
    timing_path = run_dir / "timing.json"
    return {
        "turns": parse_transcript((run_dir / "outputs" / "transcript.md").read_text()),
        "final": (run_dir / "outputs" / "final_output.md").read_text(),
        "grading": json.loads((run_dir / "grading.json").read_text())["expectations"],
        "seconds": json.loads(timing_path.read_text()).get("total_duration_seconds") if timing_path.exists() else None,
    }


def build_review_data(iteration: Path) -> dict:
    spec = json.loads((EVALS_DIR / "evals.json").read_text())
    by_name = {e["name"]: e for e in spec["evals"]}
    evals = []
    for eval_dir in sorted(iteration.glob("eval-*")):
        meta = by_name[eval_dir.name.split("-", 2)[2]]
        configs = {c.name: load_run(c / "run-1") for c in sorted(eval_dir.iterdir()) if (c / "run-1").is_dir()}
        evals.append({"dir": eval_dir.name, "name": meta["name"], "title": meta.get("title", meta["name"]),
                      "prompt": meta["prompt"], "persona": meta.get("persona", ""),
                      "expected": meta.get("expected_output", ""), "configs": configs})
    return {"skill_name": spec["skill_name"], "iteration": iteration.name.split("-")[-1], "evals": evals}


def main() -> None:
    iteration = Path(sys.argv[1])
    data = json.dumps(build_review_data(iteration)).replace("</", "<\\/")  # keep transcripts from closing the script tag
    html = (EVALS_DIR / "review_template.html").read_text().replace("__REVIEW_DATA__", data)
    out = iteration / "review.html"
    out.write_text(html)
    print(out)


if __name__ == "__main__":
    main()
