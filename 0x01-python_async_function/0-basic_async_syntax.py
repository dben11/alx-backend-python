#!/usr/bin/env python3



import asyncio
import random


"""The basics of async"""

async def wait_random(max_delay=10) -> float:
    delay =  random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    """Return the  random delay"""
    return delay 
