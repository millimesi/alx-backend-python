#!/usr/bin/env python3
'''0x01-python_async_function'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' returns after rundom time'''
    randtime = random.uniform(0, max_delay)
    await asyncio.sleep(randtime)
    return randtime
