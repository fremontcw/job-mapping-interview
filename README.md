# job-mapping-interview

A Claude skill that interviews you, one question at a time, until a job you repeat is written down well enough for an AI (or a new coworker) to do it.

## Why

When you write down how you do your job, your AI usually gets it wrong. Here's a quick test that shows why: write down one job you repeat (like the Friday report) in two minutes and hand the page to a coworker. Wherever they get stuck, your AI gets stuck too.

This skill fills those gaps under four headings:

| Heading | Question it answers |
|---|---|
| **Input** | Where does the work come from? |
| **Do** | What do you do to it, including the judgment calls? |
| **Output** | What comes out, and who gets it? |
| **Human Check** | Where does someone check it before it moves on? |

You end up with one page you can drop into a Claude Project. Test it in a fresh chat, and wherever it trips up, add that to the page's Test Log.

> Most people have never had to write down how they do their job. Mapping it is uncomfortable at first, because it shows where you've been going by feel. That isn't a personal failing. It's knowledge that has always been passed along informally, and it's worth fixing at the system level.

## Install

### claude.ai (web / desktop)
1. Download `job-mapping-interview.zip` from the [latest release](../../releases/latest).
2. In Claude, go to **Settings → Capabilities → Skills** and click **Upload skill**. Choose the zip.
3. Start a chat: *"Help me map how I do my Friday report."*

> Skills require code execution to be enabled in Settings → Capabilities.

### Claude Code
```bash
git clone https://github.com/fremontcw/job-mapping-interview
cp -r job-mapping-interview/job-mapping-interview ~/.claude/skills/
```

## Example prompts
- "My AI keeps getting our client onboarding wrong. Help me write down how I actually do it."
- "Let's do the coworker test on my weekly invoice reconciliation."
- "Here's my SOP for intake. Claude skipped the eligibility check yesterday. Patch it."

## What's inside
```
job-mapping-interview/
└── SKILL.md   # interview method, tone, and the work-map template
```

## Credits & lineage
- The **coworker test** and the Input / Do / Output / Human Check framing come from Jake Van Clief of [**Clief Notes**](https://www.skool.com/cliefnotes), which has 40+ free lessons on mapping your own work for AI.
- The four headings build on long-standing process-mapping practice: the **Input → Process → Output** model from systems analysis, Six Sigma's **SIPOC** (Suppliers, Inputs, Process, Outputs, Customers), and the human-review checkpoints used in standard operating procedures (SOPs). If your team already uses one of these, the skill works the same way. Just map its terms to the four headings.

## License
MIT
