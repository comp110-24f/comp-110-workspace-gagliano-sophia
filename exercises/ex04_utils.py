"""EX04: List Utility Functions!"""

__author__ = "730699412"


def all(list1: list[int], match: int) -> bool:
    """Returns a bool indicating if all of the ints in the list are
    the same as the given int."""
    index: int = 0
    while index < len(list1):
        if match != list[index] or len(list1) == 0:
            return False
        # must include a variable for if the list is empty
        index += 1
    return True


def max(list2: list[int]) -> int:
    """Returns the largest number in the list or a ValueError."""
    if len(list2) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 1
    remain: int = list2[index]
    while index < len(list2):
        if list2[index - 1] > list2[index]:
            remain = list2[index - 1]
            # can use pop to remove every subsequent smaller variable
            # until only the biggest variable remains
            # but we don't want to mutate the list
            # so we create another variable to replace with each larger value
        index += 1
    return remain


def is_equal(list3: list[int], list4: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    index: int = 0
    while index < len(list3):
        if list3[index] != list4[index] or len(list3) != len(list4):
            return False
        # we want to use False as a positive outcome here so that we dont
        # have to create a variable to check if every part is True
        # we can just say the whole thing is False if one is False
        # or the lists aren't the same length
        index += 1
    return True


def extend(list5: list[int], list6: list[int]) -> None:
    """Mutate the first list by appending the second list's values onto the end."""
    index: int = 0
    while index < len(list6):
        list5.append(list6[index])
        index += 1
        # just append every index onto the end
