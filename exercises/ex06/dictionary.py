"""EX06 - Dictionary Utility Functions."""

__author__ = "730699412"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Switches the keys and values of a given dict."""
    new_dict_1: dict[str, str] = {}
    for idx in dict_1:
        new_dict_1[dict_1[idx]] = idx
    if len(dict_1) != len(new_dict_1):
        raise KeyError("More than one of the same key!")
    # the original dict isn't mutated so this should easily
    # check for any repeated values
    # in the original dict
    return new_dict_1


def favorite_color(dict_2: dict[str, str]) -> str:
    """Returns the most frequent color appearance in the dict."""
    fav_color: str = ""
    dict_colors: dict[str, int] = {}
    for idx in dict_2:
        if dict_2[idx] not in dict_colors:
            dict_colors[dict_2[idx]] = 0
        if dict_2[idx] in dict_colors:
            dict_colors[dict_2[idx]] += 1
    for idy in dict_colors:
        for idz in dict_colors:
            if dict_colors[idy] < dict_colors[idz]:
                fav_color = idz
                # we can set this value to update with each new highest count
            if dict_colors[idy] == dict_colors[idz]:
                return idy
            # if the first one is equal to the second, then immediately
            # return the first value
    return fav_color


def count(list_1: list[str]) -> dict[str, int]:
    """Returns a dict of each value in the list with an associated frequency."""
    dict_store: dict[str, int] = {}
    index: int = 0
    while index < len(list_1):
        if list_1[index] in dict_store:
            dict_store[list_1[index]] += 1
            # increases the frequency value by one if it is found
        else:
            dict_store[list_1[index]] = 1
            # if it is not found, it stays as 1
        index += 1
    return dict_store


def alphabetizer(list_2: list[str]) -> dict[str, list[str]]:
    """Alphabetizes a list based on letter."""
    dict1: dict[str, list[str]] = {}
    index: int = 0
    for index in range(0, len(list_2)):
        dict1[list_2[index][0]] = []
        # adds an empty list to every spot with a key
    index = 0
    for idx in dict1:
        # this kind of for loop iterates thru dict keys
        index = 0
        while index < len(list_2):
            list_2[index].lower()
            if list_2[index][0] == idx:
                # so here instead of saying dict[idx] which would reference the value
                # you can just say idx to reference the dict key
                dict1[idx].append(list_2[index])
            index += 1
    return dict1


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Mutate dict with new attendance info."""
    if day in attendance_log:
        for person in attendance_log[day]:
            if person == student:
                return None
            # immediately return none if the person is already in the list
        attendance_log[day].append(student)
        # add the student to the list to an existing day
    else:
        list_student: list[str] = [student]
        attendance_log[day] = list_student
        # add the student to the list with the day
