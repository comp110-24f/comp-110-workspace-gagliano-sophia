"""CQ03 - While Loops Practice."""

___author___ = "730699412"


def num_instances(phrase: str, search_char: str) -> int:
    """Count the number of instances of a character within a phrase."""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
        # index and count must change by an integer to return back to the while loop
    return count
