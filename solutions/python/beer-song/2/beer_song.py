"""Beer Song"""


def plural(n: int) -> str:
    """Return the empty string if n equals 1, s otherwise."""
    return "" if n == 1 else "s"


def recite(start, take=1):
    lines = []
    for i in range(start, start - take, -1):
        # print(i)
        if i == 0:
            lines.append("No more bottles of beer on the wall, no more bottles of beer.")
            lines.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        else:
            if i == 1:
                subject = "it"
                remainder = "no more"
            else:
                subject = "one"
                remainder = i - 1
            # print(i)
            lines.append(f"{i} bottle{plural(i)} of beer on the wall, {i} bottle{plural(i)} of beer.")
            lines.append(f"Take {subject} down and pass it around, {remainder} bottle{plural(i - 1)} of beer on the wall.")
            lines.append("")

    if lines[-1] == "":
        lines = lines[:-1]
    # print(lines)
    return lines
