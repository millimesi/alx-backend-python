#!/usr/bin/env python3
"""Async comprehension"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Generate async expresion 10 times in every 10 sec'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
