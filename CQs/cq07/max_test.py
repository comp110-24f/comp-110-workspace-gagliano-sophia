"""CQ07 - Testing the find_max function."""

__author__ = "730699412"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    use_case: list[int] = [500, 3, 2, 6, 100]
    assert find_and_remove_max(use_case) == 500


def test_find_and_remove_max_2() -> None:
    use_case2: list[int] = [1, 8, 2, 3, 3]
    find_and_remove_max(use_case2)
    assert use_case2 == [1, 2, 3, 3]


def test_find_and_remove_max_3() -> None:
    edge_case: list[int] = []
    assert find_and_remove_max(edge_case) == -1


def test_find_and_remove_max_4() -> None:
    edge_case2: list[int] = [100, 2, 3, 2, 100]
    find_and_remove_max(edge_case2)
    assert edge_case2 == [2, 3, 2]
