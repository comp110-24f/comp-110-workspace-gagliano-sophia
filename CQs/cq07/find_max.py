"""CQ07 - Funcion for unit tests."""

__author__ = "730699412"


def find_and_remove_max(list1: list[int]) -> int:
    """Find and return the largest number in the input list."""
    """Remove all instances of the largest number."""
    if len(list1) == 0:
        return -1
    index: int = 0
    max_num: int = list1[0]
    while index < len(list1):
        if list1[index] > max_num:
            max_num = list1[index]
        index += 1
    index = 0
    while index < len(list1):
        if list1[index] == max_num:
            list1.pop(index)
        index += 1
    return max_num
