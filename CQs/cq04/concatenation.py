"""Concatenation file in CQ04"""

__author__ = "730699412"


def concat(string1: str, string2: str) -> str:
    """Returns the concatenation of the two input strings."""
    return string1 + string2


word1: str = "happy"
word2: str = "tuesday"


if __name__ == "__main__":
    print(concat(word1, word2))
