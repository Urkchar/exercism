"""High Scores"""


def latest(scores: list) -> int:
    return scores[-1]


def personal_best(scores: list) -> int:
    return max(scores)


def personal_top_three(scores: list) -> list:
    sorted_scores = sorted(scores, reverse=True)
    return sorted_scores[0:3]
