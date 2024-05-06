#!/usr/bin/env python3
"""Use the random module"""


import asyncio
import random


"""The basics of async"""


async def wait_random(max_delay=10) -> float:
    """Wait for some time"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
