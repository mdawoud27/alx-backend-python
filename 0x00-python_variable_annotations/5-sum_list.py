#!/usr/bin/env python3
"""
5. Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum list elements which float numbers.

    Args:
        input_list (list[float]): List of float numbers.

    Return:
        float: sum of float numbers in the list.
    """
    result: float = 0
    for num in input_list:
        result += num

    return result
