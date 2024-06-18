#!/usr/bin/env python3
"""Async comprehension"""

import random
import asyncio


async def async_generator():
    ''' Generate async expresion 10 times in every 10 sec'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
