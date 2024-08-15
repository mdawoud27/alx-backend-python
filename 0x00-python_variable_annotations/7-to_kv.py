#!/usr/bin/env python3
"""
7. Complex types - string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and a number (int or float) and returns a tuple.
    Args:
        k (str): a string
        v (int | float): a number
    Return:
        A tuple, The first element of the tuple is the string k.
        The second element is the square of the int/float v.
    """
    return (k, float(v ** 2))
