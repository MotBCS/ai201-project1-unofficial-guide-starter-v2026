# Acceptance criteria — The Unofficial Guide
Corpus: `city_guides`

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**

The five question I have written in `questions.py` cover different `city_guide` topics, including food, business hours, transportation, ticket prices, and seasons. Requiring 4 out of 5 allows one retrieval failure while still requiring the system to successfully retrieve infromation from most of the topics in the `city_guide` corpus.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**

The system answers the given questions using information retrieved from the `city_guides` corpus, so each answer has some sort of connection to each of the documents provided to the system.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

**Why this target:**

The `city_quide` corpus only contains relevant information about the topics coverd by the city guides, so questins that are asked outside those topics should not be answered using unrelated retrieved chuncks. I chose 4 out of 5 because the relevance gate should reject the out of scope questions.

Sources retrieved: guide_brightwater.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md

Is the Halden Bay seafood fresh?
  run 1: —  (best distance 0.443)
  run 2: —  (best distance 0.443)
  run 3: —  (best distance 0.443)

At what time does the Kestrelford's pub open and close?
  run 1: —  (best distance 0.402)
  run 2: —  (best distance 0.402)
  run 3: —  (best distance 0.402)

How long in minutes does it take to get from Brightwater to the regional hub?
  run 1: —  (best distance 0.290)
  run 2: —  (best distance 0.290)
  run 3: —  (best distance 0.290)

When is the cheapest time to book a ticket to the regional hub from Brightwater?
  run 1: —  (best distance 0.381)
  run 2: —  (best distance 0.381)
  run 3: —  (best distance 0.381)

When is the best time to visit?
  run 1: —  (best distance 0.503)
  run 2: —  (best distance 0.503)
  run 3: —  (best distance 0.503)

Out-of-scope questions (the gate should refuse these):
  refused  (best distance 0.887)  What is the capital of Mongolia?
  refused  (best distance 0.897)  How do I change the oil in a diesel engine?
  refused  (best distance 0.903)  Who won the 1994 World Cup?
  refused  (best distance 0.829)  What is the recommended dosage of ibuprofen for a headache?
  refused  (best distance 0.853)  How do I write a for loop in Rust?
  -> gate refused 5 of 5
  
---

## 4. Something about your chunks

For at least 4 of 5 sampled chunks that contain answers to my test questions, the chuck contains the complete information needed to anwser its corresponding question without requiring information from unrelated chunks.

**Why this target:**

My test questions include facts that may require multiple pieces of information, such as both an opening and closing time or a comparision between two booking times. These chunks need to keep related information together so that a single chuck can provide enough context to answer the given question.


---

## 5. Your choice

For at least 4 of 5 test questions that where in scope, the source document named in the final answwer contained the information that supports the answer given.

**Why this target:**

The system names a source that supports the answer it returned. I chose 4 out of 5 because one incorrect source can be allowed as long as the majority of the given test questions have correct sources.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
