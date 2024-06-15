#!/usr/bin/env python3
""" 0x00-python_variable_annotations"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    A function that returns the first element
    """

    if lst:
        return lst[0]
    else:
        return None
