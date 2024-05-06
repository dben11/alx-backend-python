#!/usr/bin/env python3
"""A module for asynchronous operations using random and asyncio."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronously wait for a random amount of time.

    Returns:
        float: The random delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
