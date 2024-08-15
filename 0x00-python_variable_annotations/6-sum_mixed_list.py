#!/usr/bin/env python3
"""
6. Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float | int]]) -> float:
    """
    Sum of the list elements

    Args:
        mxd_lst (List[float][int]): The entered list.

    Return:
        The sum of the elements int the list.
    """
    result: float = 0
    for num in mxd_lst:
        result += num

    return result
