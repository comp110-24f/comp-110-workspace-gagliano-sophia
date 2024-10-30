# def update_attendance(
#     attendance_log: dict[str, list[str]], day: str, student: str
# ) -> None:
#     """Mutate dict with new attendance info."""
#     index: int = 0
#     student_list: list[str] = []
#     while index < len(attendance_log[day]):
#         student_list.append(attendance_log[day][index])
#         index += 1
#     index = 0
#     while index < len(student_list):
#         if student_list[index] == student:
#             return None
#         index += 1
#     student_list.append(student)
#     attendance_log[day] = student_list
#     print(attendance_log)


# def update_attendance(
#     attendance_log: dict[str, list[str]], day: str, student: str
# ) -> None:
#     """Mutate dict with new attendance info."""
#     index: int = 0
#     student_list: list[str] = attendance_log[day]
#     print(attendance_log[day])
#     print(student_list)
#     while index < len(student_list):
#         if student_list[index] == student:
#             return None
#         index += 1
#     student_list.append(student)
#     attendance_log[day] = student_list


# def update_attendance(
#     attendance_log: dict[str, list[str]], day: str, student: str
# ) -> None:
#     """Mutate dict with new attendance info."""
#     for person in attendance_log[day]:
#         if person == student:
#             return None
#     attendance_log[day].append(student)


# update_attendance(
#     {"Monday": ["Alice", "Evan"], "Tuesday": ["Anna", "Eliza"]}, "Monday", "Anna"
# )


# def alphabetizer(list_2: list[str]) -> dict[str, list[str]]:
#     """Alphabetizes a list based on letter."""
#     dict1: dict[str, list[str]] = {}
#     index: int = 0
#     for index in range(0, len(list_2)):
#         dict1[list_2[index][0]] = []
#     index = 0
#     for idx in dict1:
#         index = 0
#         while index < len(list_2):
#             list_2[index].lower()
#             letter: str = list_2[index][0]
#             if letter == idx:
#                 dict1[idx].append(list_2[index])
#             index += 1
#     return dict1


# alphabetizer(["nope", "bruh", "okay", "boo", "nah"])


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
            if dict_colors[idy] == dict_colors[idz]:
                return idy
    return fav_color


favorite_color({"alice": "blue", "tom": "pink", "yolanda": "blue", "alex": "pink"})

# def favorite_color(dict_2: dict[str, str]) -> str:
#     """Returns the most frequent color appearance in the dict."""
#     color_list: list[str] = []
#     appearances: list[int] = []
#     counting_dict: dict[str, int] = {}
#     counter: int = 1
#     index: int = 0
#     indexcounter: int = 1
#     if dict_2 == {}:
#         return ""
#     for idx in dict_2:
#         color_list.append(dict_2[idx])
#     while index < len(color_list):
#         while indexcounter < len(color_list):
#             if color_list[indexcounter] == color_list[index]:
#                 counter += 1
#             indexcounter += 1
#         appearances.append(counter)
#         counter = 1
#         index += 1
#     index = 1
#     new_color_list: list[str] = []
#     while index < len(color_list):
#         if color_list[index - 1] != color_list[index]:
#             new_color_list.append(color_list[index - 1])
#         index += 1
#     index = 0
#     while index < len(new_color_list):
#         counting_dict[new_color_list[index]] = appearances[index]
#         index += 1
#     new_appearances: list[int] = []
#     for idx in counting_dict:
#         new_appearances.append(counting_dict[idx])
#     index = 0
#     most_popular: str = new_color_list[0]
#     max_appearance: int = new_appearances[0]
#     while index < len(new_appearances):
#         if new_appearances[index] > max_appearance:
#             max_appearance = new_appearances[index]
#             most_popular = new_color_list[new_appearances[index]]
#         index += 1
#     return most_popular
