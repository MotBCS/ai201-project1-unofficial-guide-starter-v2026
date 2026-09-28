# Regular expression module (used to find and replace patterns)
import re


def normalize(text):
    """Make text easier to compare."""
    return text.lower().strip()


def score_contains(answer, expected):
    """
    Check whether the expected text appears in the answer.
    """
    answer = normalize(answer)
    expected = normalize(expected)

    return expected in answer


def score_duration(answer, expected):
    """
    Compare durations such as:
        '50 minutes' == '50 min'
        '2 hours' == '2 hrs'
    """

    answer = normalize(answer)
    expected = normalize(expected)

    # Convert common time words to a standard form.
    replacements = {
        "minutes": "min",
        "minute": "min",
        "mins": "min",
        "hours": "hr",
        "hour": "hr",
        "hrs": "hr",
    }

    for old, new in replacements.items():
        answer = answer.replace(old, new)
        expected = expected.replace(old, new)

    return expected in answer


def score_time(answer, expected):
    """
    Compare clock times such as:
        '12 PM' == '12:00 PM'
        '8:30 PM' == '8:30 pm'
    """

    answer = normalize(answer)
    expected = normalize(expected)

    def normalize_time(text):
        # Convert 12:00 pm -> 12 pm
        text = re.sub(
            r"(\d{1,2}):00\s*(am|pm)",
            r"\1 \2",
            text
        )

        # Normalize spacing around AM/PM
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    answer = normalize_time(answer)
    expected = normalize_time(expected)

    return expected in answer


def score_answer(answer, expected, answer_type="contains"):
    """
    Score an AI answer using the appropriate comparison method.
    """

    if answer_type == "duration":
        return score_duration(answer, expected)

    if answer_type == "time":
        return score_time(answer, expected)

    return score_contains(answer, expected)


def calculate_score(results):
    """
    Calculate the overall evaluation score.
    """

    passed = sum(results)
    total = len(results)

    percentage = (passed / total) * 100 if total else 0

    return passed, total, percentage


def judge(question, expects, answer, results):
    """
    Decide whether an AI answer is correct.

    Returns:
        True if the answer is correct
        False if the answer is incorrect
    """

    question = normalize(question)

    # Questions asking about a journey duration.
    if "how many minutes" in question or "how long" in question:
        return score_answer(answer, expects, "duration")

    # Questions asking about opening/closing times.
    if (
        "opening" in question
        or "closing" in question
        or "hours" in question
    ):
        return score_answer(answer, expects, "time")

    # All other questions use contains matching.
    return score_answer(answer, expects, "contains")
