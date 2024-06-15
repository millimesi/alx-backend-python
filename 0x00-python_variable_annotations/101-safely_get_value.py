#!/usr/bin/env python3
""" 0x00-python_variable_annotations"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None])\
                     -> Union[Any, T]:
    """
    A function that safely gets a value from a dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
