"""EX04: List Utility Functions!"""

__author__ = "730699412"


def all(list1: list[int], match: int) -> bool:
    """Returns a bool indicating if all of the ints in the list are
    the same as the given int."""
    index: int = 0
    if len(list1) == 0:
        return False
    while index < len(list1):
        if match != list1[index]:
            return False
        # must include a variable for if the list is empty
        index += 1
    return True


def max(list2: list[int]) -> int:
    """Returns the largest number in the list or a ValueError."""
    if len(list2) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    max_num: int = list2[0]
    while index < len(list2):
        if list2[index] > max_num:
            max_num = list2[index]
        index += 1
    return max_num


# don't want to modify list, just keep track of a new number


def is_equal(list3: list[int], list4: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    index: int = 0
    correct: bool = False
    if len(list3) == len(list4):
        while index < len(list3):
            if list3[index] == list4[index]:
                correct = True
                index += 1
            else:
                correct = False
                index += 1
    if len(list3) == len(list4) == 0:
        correct = True
    return correct


# need to rewrite a False variable to keep track of when the function is equal


def extend(list5: list[int], list6: list[int]) -> None:
    """Mutate the first list by appending the second list's values onto the end."""
    index: int = 0
    while index < len(list6):
        list5.append(list6[index])
        index += 1
        # just append every index onto the end
