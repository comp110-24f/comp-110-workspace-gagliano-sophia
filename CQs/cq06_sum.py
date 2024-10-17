"""Summing the elements of a list using different loops"""

__author__ = "730699412"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of all elements with a while loop"""
    index: int = 0
    sum: float = 0.0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Returns the sum of all elements with a for in loop"""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of all elements with a for in range loop"""
    sum: float = 0.0
    for elem in range(0, len(vals)):
        sum += vals[elem]
    return sum
