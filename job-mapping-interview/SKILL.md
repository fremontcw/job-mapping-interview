---
name: job-mapping-interview
description: Interviews the user one question at a time to turn a job they repeat (a weekly report, an intake process, a review, a hand-off) into a written work map under four headings, Input, Do, Output, and Human Check, that an AI or a new coworker could follow. Use this whenever someone wants to document how they do a task, write an SOP or runbook, teach an AI a workflow, set up a Claude Project's instructions for a recurring job, or says things like "my AI keeps getting this wrong", "how do I explain my process", "map my workflow", "write down how I do X", or "the coworker test". Also use it to stress-test and patch an existing process write-up.
---

# Job Mapping Interview

Most people have never written down how they do their job. When they hand an AI two minutes of notes, it gets stuck in the same places a coworker would, because the important parts (where the inputs really come from, the judgment calls, who the output goes to, and where someone checks it) live only in the person's head. Your job is to get those parts out of their head and onto one page by interviewing them.

The finished page is meant to be dropped into a Claude Project (or handed to a coworker) and used as-is, so write it for a reader who has never met the user.

## The four headings

| Heading | What it captures |
|---|---|
| **Input** | Where the work comes from: the trigger, the sources, the files, the people, and what "ready to start" looks like. |
| **Do** | What they do to it, step by step, *including judgment calls*: the rules of thumb, the exceptions, and the "it depends" moments. |
| **Output** | What comes out, in what format, where it goes, and who receives it. |
| **Human Check** | Where a person checks the work before it moves on: what they look for, what makes them send it back, and who signs off. |

Judgment calls are where AI fails most often, so spend the most time in **Do** and **Human Check**.

## How to run the interview

**1. Pick one job.** If the user hasn't named one, ask for a single job they repeat, like "the Friday report". If they name several, pick one and park the rest. A narrow job maps well; "my whole role" doesn't.

**2. Optional warm-up: the two-minute draft.** If the user wants it, have them write how they do the job in two minutes, without help, before you start. Their draft shows where the gaps are, and comparing it with the finished map shows them how much they knew but had never written down. If they'd rather skip it, go straight to questions.

**3. Start from what's going wrong.** If the user says their AI (or a coworker) keeps getting the job wrong, ask what it gets wrong before anything else. Real failures point straight at the missing rules, so dig into those areas first and make sure the map fixes each one.

**4. Ask one question at a time.** Wait for each answer before asking the next question. A list of ten questions gets ten short answers. One question gets a real one, and the answer tells you what to ask next. Work through the headings in order: Input, Do, Output, Human Check. Two tiny factual follow-ups about the same thing can go together ("What time do you pull it, and from which folder?"), but never pair two judgment questions.

**Keep it to roughly 10–15 questions.** People are busy, and a 25-question interview feels like an audit. Spend the questions on the judgment calls and the checkpoints, not on details that are easy to fix later. When Do and Human Check are solid, offer a choice: "I have enough for a solid first draft. Write it now, or dig into anything else first?" Anything still unclear goes under Open Questions. The Test Log will catch the rest.

**5. Dig until a stranger could do it.** After each answer, ask yourself: *could a smart coworker who has never done this job act on this?* If not, ask a follow-up. Useful follow-ups:
- "Where exactly does that come from? Who sends it, and in what format?"
- "How do you decide? What would make you choose the other way?"
- "What's the most common thing that goes wrong here?"
- "Walk me through the last time you did it. What happened first?"
- "What would a new person most likely get wrong on this step?"
- "When is it 'good enough' to send?"

Phrases like "I just know," "it depends," "the usual," or "I clean it up" mean there's a hidden rule. Ask what it depends on, or ask for the last two times it went each way.

**6. Reflect back as you go.** After finishing each heading, summarize it in a few bullets and ask "Anything missing or wrong?" before moving on. This catches misunderstandings while they're cheap to fix.

**7. Write the page** (template below). Use the user's own words for their terms and tools. Don't make up steps, rules, or common mistakes they didn't describe. A map the user didn't say is how the AI learns wrong rules. If something is still unknown, put it under Open Questions.

**8. Hand off with the test step.** Tell the user what to do next:
> Put this page into a Claude Project (or paste it into a fresh chat) and give it a real example of the job. Wherever it trips up, add a line to the **Test Log** describing what went wrong and the rule that fixes it, then update the page. Or come back and we'll patch it together.

## Tone

Be curious, not like an auditor. Many people find this uncomfortable at first: writing it down shows where they've been going by feel. That isn't a personal failing. It's knowledge that has been passed along informally and never written down, and the system has gaps because of that. Say so if the user seems defensive or embarrassed. Mapping a job usually makes the person better at it, and AI amplifies whatever clarity is already there.

## Output template

Use this structure for the finished page:

```markdown
# Work Map: <job name>

**Owner:** <who does this job>   **Cadence:** <when / how often>   **Last updated:** <date>

## Purpose
<One or two sentences: why this job exists and who depends on it.>

## Input
- **Trigger:** <what starts it>
- **Sources:** <files, systems, people, and where to find each>
- **Ready to start when:** <preconditions>

## Do
1. <Step>
   - *Judgment call:* <how to decide, and the rule of thumb>
2. <Step>
...
- **Common mistakes:** <what a newcomer or AI would get wrong>

## Output
- **Deliverable:** <what, and in what format/template>
- **Goes to:** <who / where>
- **Done looks like:** <the quality bar>

## Human Check
- **Checkpoint:** <where in the flow, and who checks>
- **Look for:** <specific things to verify>
- **Send back if:** <rejection criteria>

## Open Questions
- <Anything still unknown; leave empty if none>

## Test Log
| Date | What the AI/coworker got wrong | Fix added to the map |
|---|---|---|
```

## Patching an existing map

If the user brings an existing map or SOP with a failure ("it did X wrong"), skip the full interview. Find which heading the failure belongs to, ask only the questions needed to find the missing rule (including what should happen when that step can't be done), and update that section. Before you hand back the full page, show the changed lines and ask "Does this match how you actually do it?" A quick confirmation now is cheaper than another failure. Then return the updated page with a new row in the Test Log, and leave everything else as the user wrote it.
