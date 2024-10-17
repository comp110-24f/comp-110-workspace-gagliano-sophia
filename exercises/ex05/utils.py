"""EX05 - List utility functions."""

__author__ = "730699412"


def only_evens(list1: list[int]) -> list[int]:
    """Returns a list of only the even elements in a list."""
    index: int = 0
    list1_count: list[int] = []
    while index < len(list1):
        if list1[index] % 2 == 0:
            # remainder of 0 is an even number
            list1_count.append(list1[index])
        index += 1
    return list1_count


def sub(list2: list[int], start: int, end: int) -> list[int]:
    """Generating a list of the values between a start and end point."""
    list2_count: list[int] = []
    index: int = 0
    new_end: int = end
    new_start: int = start
    if len(list2) == 0:
        return []
    if start >= len(list2):
        return []
    if start < 0:
        new_start = 0
    if end > len(list2):
        end = len(list2)
        index = new_start
        while index < end:
            list2_count.append(list2[index])
            index += 1
    if end < len(list2):
        index = new_start
        while index < new_end:
            list2_count.append(list2[index])
            index += 1
    # had to add a separate if statement for when the end is greater than the length
    # of the list
    # we are looking for an end that is one less than the
    # specification in parameters
    return list2_count


# passes my tests! needed multiple lines for each weird case


def add_at_index(list3: list[int], elem_add: int, index_add: int) -> None:
    """Modifies list to add an element at a specific index."""
    if index_add > len(list3):
        raise IndexError("Index is out of bounds for the input list")
    if index_add < 0:
        raise IndexError("Index is out of bounds for the input list")
    indexoriginal: int = len(list3)
    list3.append(0)
    # add an extra element to the end of the list
    index: int = len(list3)
    indexcounter: int = index_add
    while index > index_add:
        if indexcounter < indexoriginal:
            list3.append(list3[indexcounter])
        index -= 1
        indexcounter += 1
        # adding all values after and including the add point to the end
        # of the list in order
    index = index_add + 1
    indexcounter = index_add
    while index <= indexoriginal:
        list3.pop(indexcounter + 1)
        index += 1
        # removing every unneeded value between the add point and the 0 point
    list3[index_add] = elem_add
    # replaces 0 with the desired value
