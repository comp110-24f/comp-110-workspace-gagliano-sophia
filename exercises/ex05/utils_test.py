"""EX05 - Testing list utility functions."""

__author__ = "730699412"

from exercises.ex05.utils import only_evens, sub, add_at_index

import pytest


def test_only_evens_1() -> None:
    """Tests if the function returns the correct list of values."""
    use_case: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(use_case) == [2, 4, 6]


def test_only_evens_mutation() -> None:
    """Tests if the function does not mutate the original list."""
    use_case_mutation: list[int] = [100, 2, 3, 7]
    only_evens(use_case_mutation)
    assert use_case_mutation == [100, 2, 3, 7]
    # this shouldn't mutate the input parameter list


def test_only_evens_empty() -> None:
    """Tests if an empty list is returned given a list of all odd numbers."""
    edge_case: list[int] = [1, 3, 7, 9]
    assert only_evens(edge_case) == []
    # edge case with no even numbers in the list should return an empty list


def test_sub_1() -> None:
    """Tests if the proper sub list is returned within the parameters specified."""
    use_case: list[int] = [8, 29, 2, 34]
    assert sub(use_case, 1, 3) == [29, 2]
    # make sure index 3 is not included in the return


def test_sub_mutation() -> None:
    """Tests if the function does not mutate the original list."""
    use_case_mutation: list[int] = [100, 2, 3, 42, 46, 87, 3, 25]
    sub(use_case_mutation, 2, 7)
    assert use_case_mutation == [100, 2, 3, 42, 46, 87, 3, 25]


def test_sub_start_negative() -> None:
    """Tests if the function returns the correct list if the start is negative."""
    edge_case: list[int] = [1, 2, 3, 4, 252, 573, 21]
    assert sub(edge_case, -2, 3) == [1, 2, 3]
    # make sure index 3 is not included in the return


def test_sub_end_large() -> None:
    """Tests if the function returns the correct list if the end is larger than the list length."""
    edge_case_2: list[int] = [2, 3, 2, 123, 3, 234, 1]
    assert sub(edge_case_2, 0, 9) == [2, 3, 2, 123, 3, 234, 1]


def test_add_at_index_1() -> None:
    """Tests if the function properly returns None."""
    use_case: list[int] = [102, 392, 32, 3, 42, 1]
    assert add_at_index(use_case, 2, 1) is None


def test_add_at_index_mutation() -> None:
    """Tests if the function mutates the list correctly."""
    use_case_mutation: list[int] = [1002, 3, 2, 34]
    add_at_index(use_case_mutation, 92, 2)
    assert use_case_mutation == [1002, 3, 92, 2, 34]
    # this just checks the original list


def test_add_at_index_indexerror():
    """Tests if the function raises the Index Error for the proper specifications."""
    edge_case: list[int] = [1, 2, 3, 42, 24, 4, 5]
    with pytest.raises(IndexError):
        add_at_index(edge_case, 8, -1)
        # -1 is out of bounds for a position to add
