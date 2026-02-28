"""Scrabble Score"""

def score(word: str) -> int:
    # Normalize case
    word = word.upper()

    score = 0
    for letter in word:
        if letter in ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T"):
            score += 1
        elif letter in ("D", "G"):
            score += 2
        elif letter in ("B", "C", "M", "P"):
            score += 3
        elif letter in ("F", "H", "V", "W", "Y"):
            score += 4
        elif letter == "K":
            score += 5
        elif letter in ("J", "X"):
            score += 8
        elif letter in ("Q", "Z"):
            score += 10
        else:
            raise ValueError(f"Unexpected character encountered: '{letter}'")

    return score
