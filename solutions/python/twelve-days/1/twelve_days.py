"""Twelve Days"""

LINES = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves,",
    "three French Hens,",
    "four Calling Birds,",
    "five Gold Rings,",
    "six Geese-a-Laying,",
    "seven Swans-a-Swimming,",
    "eight Maids-a-Milking,",
    "nine Ladies Dancing,",
    "ten Lords-a-Leaping,",
    "eleven Pipers Piping,",
    "twelve Drummers Drumming,"
]

DAYS = {
    1 : "first",
    2 : "second",
    3 : "third",
    4 : "fourth",
    5 : "fifth",
    6 : "sixth",
    7 : "seventh",
    8 : "eighth",
    9 : "ninth",
    10 : "tenth",
    11 : "eleventh",
    12 : "twelfth"
}


def recite(start_verse: int, end_verse: int) -> list:
    result = []
    for i in range(start_verse, end_verse + 1):
        result.append(f"On the {DAYS[i]} day of Christmas my true love gave to me: " + " ".join(LINES[i-1::-1]))

    # Add an "and" for all verses after the first
    for i, element in enumerate(result):
        if "two" in element:
            result[i] = element.replace("a Partridge in a Pear Tree.", "and a Partridge in a Pear Tree.")

    return result
