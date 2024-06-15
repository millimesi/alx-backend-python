#!/usr/bin/env python3
""" 0x00-python_variable_annotations"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Take two args and return float and str tuple'''
    return (k, v**2)
