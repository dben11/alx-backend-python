#!/usr/bin/env python3
"""
Using the asynchronous module and the random module.
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Generate n delays asynchronously with a maximum delay of max_delay.

    :param n: The number of delays to generate.
    :param max_delay: The maximum delay value.
    :return: A list of delays in ascending order.
    """
    tasks = []
    delays = []

    # Create tasks to generate delays
    for _ in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    # Wait for tasks to complete and collect delays
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    # Sort delays in ascending order
    return sorted(delays)
