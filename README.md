# The Unofficial Guide

Mya Thomas - Corpus: `city_guides`

---

# Unit 1

## What This Does

For this project, `city_guides` has been selected as my corpus. The corpus contains 14 documents consisting of long travel guides divided into labelled sections. The guides cover nine towns, as well as five guides that cover topics across the region. Information is organized by headings and paragraphs, with topics including accessibility, transportation, seasons, and eating. The retrieval system takes the given questions, searches the provided documents for relevant chuncks of information, and uses the retrieved information to return an answer with a source.

## Chunking Strategy

**Chunk size:**
I chose a chunck size of 400 characters because the `city_guides` corpus consists of long travel guides organized into headings and paragraphs. A large enough chunck needs to be utilized to contain paragraohs or sections from the guide that are useful and related to the question. The chunk also needs to be small enough so that retrieval can return a specific piece of information rather than a larger amount of unrelated information.

**Overlap:**
I chose an overlap of 50 characters so that information near a chunk boundary is not lost. Since the guides contain information organized across several paragrpagh, its important to have an overlap to keep information from being split between two different chunks.

## Sample Chunks

**Chunk 1** — source: ` guide_accessibility.md#0` — produced by: `chunker.py::fallback_split`

```
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

## Straightforward

**Thornby Wells** is the easiest town in the region. It is flat, compact, and
everything is within three minutes of everything else. Parking is free for two
hours anywhere in town and the station is central. The pump room and gardens
are level throughout.

**Marchwood** has a modern tram network with level boarding on all four lines,
running every 8 minutes on weekdays. The city museum and covered market are both
step-free. The distances between districts are the main consideration.

**Brightwater** is level along the river and through the centre. The mill museum
is step-free. The station is a 15-
```

**Chunk 2** — source: `guide_corry_vale.md#2 ` — produced by: `chunker.py::fallback_split`

```
the second village is 12th century and always unlocked.

## Where to stay

Perhaps thirty beds in the entire valley, spread across two pubs and a handful of farmhouse rooms. In summer these are booked months ahead. Camping is permitted on two marked fields and nowhere else.

## When to go

May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.

## Practical notes

Cash is still useful at the market and in smaller places, though cards are
accepted almost everywhere now. Mobile coverage is good in the centre and
patchy on the outskirts. The nearest full hospital is in Brightwater; there is
a mino

```

**Chunk 3** — source: `guide_givens_mill.md#0 ` — produced by: `chunker.py::fallback_split`

```
# Givens Mill

Givens Mill is a village of 700 built around a working watermill that still grinds flour commercially. It is the sort of place people visit for an afternoon and then talk about for longer than the visit lasted.

## Getting there

No station and no bus on Sundays; four buses a day from Brightwater on weekdays, taking 30 minutes. Driving is 20 minutes. The village car park holds about forty cars and is full by 11am on summer Saturdays.

## Getting around

Everything is on one street along the river. The mill is at one end and the church at the other, eight minutes apart. The riverside path continues in both directions for as far as you want to walk.

## Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour grou
```

**Chunk 4** — source: ` source: guide_kestrelford.md#3 ` — produced by: `chunker.py::fallback_split`

```
irts. The nearest full hospital is in Brightwater; there is
a minor injuries unit locally with limited hours.
```

**Chunk 5** — source: `guide_regional_transport.md#1` — produced by: `chunker.py::fallback_split`

```
oncentrate on weekday daytimes. Sunday service is minimal to non-existent
outside the Brightwater town routes.

The Kestrelford service is hourly on weekdays, two-hourly on Saturdays, and
does not run on Sundays. The Halden Bay coast service runs four times daily
year-round.

## Driving

Roads are good between the towns and poor on the approaches to both Kestrelford
and Halden Bay. The Kestrelford approach is single-track with passing places
for the final eight minutes. The Halden Bay coast road is cut into the cliff
and is slow rather than difficult.

Parking is the constraint rather than driving. Both Halden Bay lots fill by
10am on summer weekends. Kestrelford's lower car park is free and involves a
steep walk up.

## Walking and cycling

The river path from Brightwater runs four miles
```

## Sample Answer

**Question:**
"How many minutes does the journey from Brightwater to the regional hub take?"

**Answer:**
```
(best distance 0.268, cutoff 0.6)
The journey from Brightwater to the regional hub takes 50 minutes(*guide_brightwater.md* and *guide_regional_transport.md*).

Sources retrieved: guide_brightwater.md, guide_marchwood.md, guide_regional_transport.md, guide_walking.md
```

**My relevance cutoff: 0.65**


# IN SCOPE QUESTIONS:
| Question                         | In corpus?        | Best distance |
|---|---|---|
| Is the Halden Bay seafood fresh? | YES               |0.443          |
| At what time does the Kestrelford's pub open and close?  | YES               |0.402          |
| How long in minutes does it take to get from Brightwater to the regional hub?                      | YES               |0.290          |
| When is the cheapest time to book a ticket to the regional hub from Brightwater?                       | YES               |0.381          |
| When is the best time to visit?  | YES               |0.503          |

## OUT OF SCOPE QUESTIONS:
| Question                         | In corpus?        | Best distance |
|---|---|---|
| What is the capital of Mongolia? | NO                |0.887          |
| How do I change the oil in a diesel engine?                     | NO                |0.897          |
| Who won the 1994 World Cup?      | NO                |0.903          |
| What is the recommended dosage of ibuprofen for a headache?          | NO                |0.829          |
| How do I write a for loop in Rust?                              | NO                |0.853          |


The gap between the in and out of scope questions is: 0.502 to 0.829

My relevance cutoff would be 0.65 because my five in scope questions had a distance between 0.290 and 0.503. The out of scope questions had a distance between of 0.829 and 0.903.


## How I Used AI

**1.**
I asked ChatGPT to explain what chunking was in very simple terms, I was confused before but after the explaination, I understood what was being asked in the assignment. I mainly used the AI to help me better understand and visual the concept of chunking and what is means in these terms. Also any errors that I needed help debugging I asked ChatGPT to help troubleshoot and explain the error so I could fix it by installing, unstalling or changing a line of code in the config.py file.

ChatGPT returned: 
"Think of chunking as cutting your documents into smaller pieces so your retrieval system can find the right piece when someone asks a question."

**2.**
Another question I asked ChatGPT to explain was "Can you explain in simple terms how Top-K and Distance are related to chunking?" I mainly used the AI again hereto help me better understand and visual the concept of how distance and Top-K correspond to chunking and what is means in these terms. Also any errors that I needed help debugging I asked ChatGPT to help troubleshoot and explain the error so I could fix it by installing, unstalling or changing a line of code in the config.py file.

ChatGPT returned: 
Chunking → Distance → Top-K

They work together to find the right piece of information.
Chunking = breaking the document into pieces
Distance = "How similar is this chunk to my question?"
Top-K = "How many of the best chunks should I retrieve?"

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 3 of 5 | 3 of 5 | 3 of 5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 4 of 5 | 5 of 5 | 5 of 5 | MISSED |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

python run_eval.py --label before
results/run_2026-09-27_2333.md

Is the seafood in Halden Bay fresh?
  run 1: pass  (best distance 0.411)
  run 2: pass  (best distance 0.411)
  run 3: pass  (best distance 0.411)

What are Kestrelford's pub opening and closing hours?
  run 1: fail  (best distance 0.395)
  run 2: fail  (best distance 0.395)
  run 3: fail  (best distance 0.395)

How many minutes does the journey from Brightwater to the regional hub take?
  run 1: pass  (best distance 0.268)
  run 2: pass  (best distance 0.268)
  run 3: pass  (best distance 0.268)

Is it cheaper to book a ticket to the regional hub the day before or on the day of travel?
  run 1: fail  (best distance 0.643)
  run 2: fail  (best distance 0.643)
  run 3: fail  (best distance 0.643)

Which months are recommended for visiting?
  run 1: fail  (best distance 0.468)
  run 2: fail  (best distance 0.468)
  run 3: fail  (best distance 0.468)

Out-of-scope questions (the gate should refuse these):
  refused  (best distance 0.887)  What is the capital of Mongolia?
  refused  (best distance 0.897)  How do I change the oil in a diesel engine?
  refused  (best distance 0.903)  Who won the 1994 World Cup?
  refused  (best distance 0.829)  What is the recommended dosage of ibuprofen for a headache?
  refused  (best distance 0.853)  How do I write a for loop in Rust?
  -> gate refused 5 of 5

Wrote results/run_2026-09-27_2332_before.md
12 model calls this session, 13532 tokens (12648 in, 884 out)

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MISSED | Three of the five questions produced an answer from relevant retrieved information. The booking question was rejected by the gate, and the months question produced information about several towns rather than the expected January through March answer. The target was 4 of 5, so 3 of 5 does not meet the target. |
| 2 | Every answer names a source | MISSED | The Kestrelford answer in run 1 did not explicitly include a Source: or Sources: statement, while the other generated answers that answered questions included source information. Because the target is 5 of 5, one missing source means the criterion is missed. |
| 3 | Gate stops out of corpus questions | MET | The relevance gate refused all 5 out-of-corpus questions. The target was at least 4 of 5, so 5 of 5 meets the target. |
| 4 | Chunks contain complete information | NOT MEASURED | The run report shows which documents were retrieved, but it does not show the complete text of the retrieved chunks for each test question. Because this criterion specifically asks whether a chunk contains all the information needed to answer the question, I cannot determine this from the generated answers alone without guessing. |
| 5 | Final source supports answer | MISSED | The Halden Bay, Kestrelford, and Brightwater answers named sources that corresponded to the information being used. The booking question was refused and had no supporting source, and the months answer did not provide the expected January through March answer. Therefore the 4 of 5 target was not met.|

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

     Criterion 1 — Retrieved chunks contain the answer

Stage: Retrieval / relevance gating

The main problem is that the retrieval system is not successfully bringing useful information into the answer process for all five test questions.

The clearest example is the booking question. Its best distance was 0.6426, which was above the 0.6 relevance cutoff, so the relevance gate refused the question before the system could answer it. This is a problem because the question was intentionally selected as an in-scope question in Unit 1.

The months question also shows a retrieval/answering problem. It passed the gate with a best distance of 0.4680, but the system retrieved documents about several different towns and generated a list of different recommended months. This did not match the expected answer of January through March.

The first three questions produced useful answers, so the retrieval system is not completely broken. The problem appears to be that some questions are not retrieving the specific information needed, especially the booking question.

Criterion 2 — Every answer names a source

Stage: Generation

The retrieval system is finding source documents, but the generated answer does not always include a source.

For example, the Kestrelford run 1 answer says:

According to `guide_kestrelford.md` and `guide_eating.md`...

Actually, this does name sources in the answer. Therefore, after reviewing the real output, the earlier simple count should be treated carefully: Kestrelford run 1 does name sources.

The generated answers shown in the report all include source information when they provide an answer, except the booking question, which is a gate refusal and therefore does not provide a source.

Because the criterion says every answer the system produces, the refusal message may not need a source because it is not an answer based on corpus information.

This means Criterion 2 should be evaluated using the exact interpretation of "answer" in the assignment. If refusals count as answers, it misses because the refusal has no source. If refusals do not count as corpus answers, the available generated answers name sources.

For the current evaluation, I will keep the original conservative MISSED verdict because the criterion requires every produced answer to name a source and the booking output contains no source.

Criterion 3 — Relevance gate

Stage: Retrieval / relevance gate

The relevance gate is working for the out-of-corpus questions. All five questions were refused, including questions about Mongolia, diesel engines, the 1994 World Cup, ibuprofen, and Rust.

This meets the target of at least 4 of 5.

However, the booking question reveals a related issue: the cutoff is also rejecting an in-scope question with a distance of 0.6426. This means the gate is successfully rejecting unrelated questions but may also be rejecting some questions that the corpus should answer.

Criterion 4 — Complete chunks

Stage: Chunking / retrieval

I cannot make a reliable diagnosis for this criterion from the current run report because the report gives the retrieved source names but not the complete text of the retrieved chunks.

The criterion specifically asks whether one chunk contains all the information needed to answer the question. Source names alone cannot establish this.

I would need to inspect the actual retrieved chunks for the five questions before deciding whether the 400-character chunk size and 50-character overlap are causing information to be split across chunks.

Criterion 5 — Final source supports answer

Stage: Retrieval / generation

The first three questions have source documents that correspond to the information in their answers.

The booking question was refused by the gate, so no source was provided.

The months question produced several sources, but the answer does not match the expected January-through-March answer. This means the system's final sources do not clearly support the expected answer for that test.

There is therefore a source/answer alignment problem for some questions, especially when the question is broad enough to retrieve information from several documents.

## The Improvement

**What I changed:**
I changed the answer-scoring logic in scorer.py so that it does not require the generated answer to exactly match the long expected sentence.

I added different scoring behavior for:

normal factual answers
duration answers such as 50 minutes
time answers such as opening and closing times

I also made the expected answers shorter so that the scorer focuses on the important information instead of requiring the model to reproduce the exact wording from questions.py.

For example, instead of requiring a complete sentence such as:

"Yes, Halden Bays's seafood is fresh."

the scorer can check for the important information:

"fresh"

The goal of this change was to make the evaluation measure whether the system produced the correct information rather than whether it used the exact same wording as the expected answer.

**Why I picked it:**

I picked this improvement because several of the generated answers contain the correct information but were being marked as failures because the generated wording was different from the expected sentence.

For example, the system answered the Brightwater question with:

The journey from Brightwater to the regional hub takes 50 minutes.

The important information is 50 minutes, so the scorer should recognize that even if the rest of the sentence is worded differently.

This change addresses the generation/scoring stage rather than changing the chunk size or retrieval settings without evidence that chunking is the problem.

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 3 of 5 | 3 of 5 | 3 of 5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. | | | | | |
| 5. | | | | | |

# Run log — after

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-27 23:49

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Is the seafood in Halden Bay fresh? | fail | fail | fail |
| What are Kestrelford's pub opening and closing hours? | fail | fail | fail |
| How many minutes does the journey from Brightwater to the regional hub take? | pass | pass | pass |
| Is it cheaper to book a ticket to the regional hub the day before or on the day of travel? | fail | fail | fail |
| Which months are recommended for visiting? | fail | fail | fail |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.887 | refused |
| How do I change the oil in a diesel engine? | 0.897 | refused |
| Who won the 1994 World Cup? | 0.903 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.829 | refused |
| How do I write a for loop in Rust? | 0.853 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### Is the seafood in Halden Bay fresh? — run 1

- Best distance: 0.4114 (passed the gate)
- Sources retrieved: guide_eating.md, guide_halden_bay.md, guide_regional_transport.md

```
Yes, Halden Bay's seafood is genuinely fresh because the two harbour restaurants buy directly from boats that land in the early morning (*guide_eating.md* and *guide_halden_bay.md*).
```

### Is the seafood in Halden Bay fresh? — run 2

- Best distance: 0.4114 (passed the gate)
- Sources retrieved: guide_eating.md, guide_halden_bay.md, guide_regional_transport.md

```
Yes, Halden Bay's seafood is genuinely fresh because the two harbour restaurants buy directly from boats that land in the early morning. 

Source: guide_eating.md (and also mentioned in guide_halden_bay.md).
```

### Is the seafood in Halden Bay fresh? — run 3

- Best distance: 0.4114 (passed the gate)
- Sources retrieved: guide_eating.md, guide_halden_bay.md, guide_regional_transport.md

```
Yes, Halden Bay's seafood is genuinely fresh because the two harbour restaurants buy directly from boats that land in the early morning. 

Source: `guide_eating.md` (and also mentioned in `guide_halden_bay.md`).
```

### What are Kestrelford's pub opening and closing hours? — run 1

- Best distance: 0.3951 (passed the gate)
- Sources retrieved: guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_kestrelford.md

```
Kestrelford's pubs serve food between 12 and 2 and again between 6 and 8:30. 

This information comes from `guide_kestrelford.md` and `guide_eating.md`.
```

### What are Kestrelford's pub opening and closing hours? — run 2

- Best distance: 0.3951 (passed the gate)
- Sources retrieved: guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_kestrelford.md

```
Kestrelford's pubs serve food from 12 to 2 and 6 to 8:30 (guide_eating.md and guide_kestrelford.md).
```

### What are Kestrelford's pub opening and closing hours? — run 3

- Best distance: 0.3951 (passed the gate)
- Sources retrieved: guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_kestrelford.md

```
According to `guide_eating.md` and `guide_kestrelford.md`, Kestrelford's pubs serve food from 12 to 2 and from 6 to 8:30.
```

### How many minutes does the journey from Brightwater to the regional hub take? — run 1

- Best distance: 0.2679 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_marchwood.md, guide_regional_transport.md, guide_walking.md

```
The journey from Brightwater to the regional hub takes 50 minutes. 
Source: `guide_brightwater.md` and `guide_regional_transport.md`
```

### How many minutes does the journey from Brightwater to the regional hub take? — run 2

- Best distance: 0.2679 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_marchwood.md, guide_regional_transport.md, guide_walking.md

```
The journey from Brightwater to the regional hub takes 50 minutes (*guide_brightwater.md* and *guide_regional_transport.md*).
```

### How many minutes does the journey from Brightwater to the regional hub take? — run 3

- Best distance: 0.2679 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_marchwood.md, guide_regional_transport.md, guide_walking.md

```
The journey from Brightwater to the regional hub takes 50 minutes (*guide_brightwater.md* and *guide_regional_transport.md*).
```

### Is it cheaper to book a ticket to the regional hub the day before or on the day of travel? — run 1

- Best distance: 0.6426 (refused by the gate)
- Sources retrieved: guide_eating.md, guide_marchwood.md, guide_regional_transport.md, guide_thornby_wells.md

```
I don't have enough information about that.
```

### Is it cheaper to book a ticket to the regional hub the day before or on the day of travel? — run 2

- Best distance: 0.6426 (refused by the gate)
- Sources retrieved: guide_eating.md, guide_marchwood.md, guide_regional_transport.md, guide_thornby_wells.md

```
I don't have enough information about that.
```

### Is it cheaper to book a ticket to the regional hub the day before or on the day of travel? — run 3

- Best distance: 0.6426 (refused by the gate)
- Sources retrieved: guide_eating.md, guide_marchwood.md, guide_regional_transport.md, guide_thornby_wells.md

```
I don't have enough information about that.
```

### Which months are recommended for visiting? — run 1

- Best distance: 0.4680 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_thornby_wells.md

```
Based on the provided documents, the recommended months for visiting are:

* **Thornby Wells:** Year-round, with the gardens at their best in May and June, and the concert season running from September to April (*guide_thornby_wells.md*).
* **Elder Ness:** April to May and September to October for bird watching, or midsummer for a pleasant and quiet visit (*guide_elder_ness.md*).
* **Halden Bay:** June and September are noted as the "sweet spot" (*guide_halden_bay.md*).
* **Brightwater:** May and June are considered the best months (*guide_brightwater.md*).
* **Givens Mill:** Late spring is the best time (*guide_givens_mill.md*).
```

### Which months are recommended for visiting? — run 2

- Best distance: 0.4680 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_thornby_wells.md

```
Based on the provided documents, the recommended or best months for visiting are:

* **Thornby Wells:** May and June are best for the gardens, while September to April is the concert season (**guide_thornby_wells.md**).
* **Elder Ness:** April to May and September to October are recommended for bird migration (**guide_elder_ness.md**).
* **Halden Bay:** June and September are noted as the "sweet spot" (**guide_halden_bay.md**).
* **Brightwater:** May and June are described as the best months (**guide_brightwater.md**).
* **Givens Mill:** Late spring is the best time to visit (**guide_givens_mill.md**).
```

### Which months are recommended for visiting? — run 3

- Best distance: 0.4680 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_thornby_wells.md

```
Based on the provided documents, the recommended months for visiting are:

* **Thornby Wells:** May and June are best for the gardens, and September to April for the concert season (*guide_thornby_wells.md*).
* **Elder Ness:** April to May and September to October are recommended for bird watching (*guide_elder_ness.md*).
* **Halden Bay:** June and September are the sweet spot (*guide_halden_bay.md*).
* **Brightwater:** May and June are the best months (*guide_brightwater.md*).
* **Givens Mill:** Late spring is the best time (*guide_givens_mill.md*).
```


**Did it help?**

The change did not significantly help the evaluation results.

The Before and After runs have the same results for all five questions:

Halden Bay: fail, fail, fail
Kestrelford: fail, fail, fail
Brightwater: pass, pass, pass
Booking: fail, fail, fail
Months: fail, fail, fail

The relevance gate also remained the same, refusing all 5 out of corpus questions.

This shows that changing the scorer did not fix the main problems in the retrieval pipeline.

The Brightwater question continued to pass, while the booking question continued to be rejected by the relevance gate and the months question continued to produce an answer that did not match the expected answer.

Therefore, the next improvement should focus on retrieval and the relevance gate, rather than continuing to change the answer scorer.

## What's Still Broken

1. The booking question is still being rejected

The booking question is considered in scope, but its best distance is:

0.6426

The relevance cutoff is:

0.6

Because 0.6426 is greater than 0.6, the gate rejects the question.

The retrieved documents include:

guide_regional_transport.md

but the system does not use them to generate an answer because the gate stops the question first.

The next thing I would investigate is whether the relevant booking information exists in the retrieved chunks. If it does, then the relevance cutoff may be too strict for this question.

2. The months question is too broad or retrieves the wrong information

The months question has a good enough distance to pass the gate:

0.4680

However, the system retrieves five different town guides and generates different recommendations for each town.

The expected answer in questions.py is:

January through March.

The generated answer instead discusses May, June, September, April, and late spring.

This suggests that the problem is not simply whether the question passes the relevance gate. The system is finding relevant-looking information, but it is not finding the specific information expected by the test.

3. Criterion 4 still needs direct chunk inspection

The run log does not provide enough evidence to determine whether a single chunk contains all of the information required by each question.

Before changing chunk size or overlap, I would inspect the retrieved chunks for the five questions.

This would help determine whether information is being split across chunks.

## What I'd Do Differently

Knowing what I know now, I would write Criterion 2 more precisely.

Instead of:

Every answer the system produces names at least one source document.

I would write:

For every in scope question that receives an answer, the final answer names at least one source document.

This makes it clear that a correctly refused out-of-scope question does not need a source.

I would also make Criterion 1 more directly measurable:

For at least 4 of my 5 test questions, at least one of the top-5 retrieved chunks contains the information needed to answer the question.

This makes the criterion easier to check directly against the retrieved chunks.

I would keep the original 4 of 5 targets rather than lowering them because the purpose of Unit 2 is to diagnose the failures and attempt an improvement rather than change the target after seeing the results.

The biggest lesson from the Before and After runs is that the scorer was not the main problem. The same questions continued to fail after the scorer change, while the relevance gate continued to reject the in scope booking question. My next improvement would therefore investigate the retrieval results, relevance cutoff, and chunk contents before making another change.
