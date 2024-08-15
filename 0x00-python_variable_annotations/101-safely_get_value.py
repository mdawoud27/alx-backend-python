#!/usr/bin/env python3
"""11. More involved type annotations"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, T],
        key: Any,
        default: Union[T, None] = None
) -> Union[T, None]:
    """
    Safely get the value from a dictionary by key, returning a default value
    if the key is not found.
    Args:
        dct (Mapping[Any, T]): The dictionary from which to retrieve
        the value.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None]): The default value to return if
        the key is not found.

        Returns:
            Union[T, None]: The value associated with the key
            if found, otherwise the default value.
        """
    if key in dct:
        return dct[key]
    else:
        return default
