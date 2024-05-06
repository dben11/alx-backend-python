#!/usr/bin/env python3
"""
Using the Asynchronous module, the random and the async module

"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay) -> List[float]:
    """
    Import the wait_random function
    Defin an async routine named wait_n
    Returns a list of delays in asc order

    """
    tasks = []
    delays = []


    for i in range(n):
        task = wait_random(max_delay)
        tasks.append(task)


    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)


    return delays
