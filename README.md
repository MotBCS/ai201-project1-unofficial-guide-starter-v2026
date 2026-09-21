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

**My relevance cutoff:**


## IN SCOPE QUESTIONS:
| Question                         | In corpus?        | Best distance |
-------------------------------------------------------------------------------
| Is the Halden Bay seafood fresh? | YES               |0.443          |
-------------------------------------------------------------------------------
| At what time does the 
Kestrelford's pub open and close?  | YES               |0.402          |
-------------------------------------------------------------------------------
| How long in minutes does it take 
to get from Brightwater to the 
regional hub?                      | YES               |0.290          |
-------------------------------------------------------------------------------
| When is the cheapest time to book 
a ticket to the regional hub from 
Brightwater?                       | YES               |0.381          |
-------------------------------------------------------------------------------
| When is the best time to visit?  | YES               |0.503          |
-------------------------------------------------------------------------------

## OUT OF SCOPE QUESTIONS:
| Question                         | In corpus?        | Best distance |
-------------------------------------------------------------------------------
| What is the capital of Mongolia? | NO                |0.887          |
-------------------------------------------------------------------------------
| How do I change the oil in a
diesel engine?                     | NO                |0.897          |
-------------------------------------------------------------------------------
| Who won the 1994 World Cup?      | NO                |0.903          |
-------------------------------------------------------------------------------
| What is the recommended dosage of 
ibuprofen for a headache?          | NO                |0.829          |
-------------------------------------------------------------------------------
| How do I write a for loop in 
Rust?                              | NO                |0.853          |
-------------------------------------------------------------------------------

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
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

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

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
