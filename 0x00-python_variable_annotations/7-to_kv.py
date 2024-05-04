#!/usr/bin/env python3
"""Complex types-string and int/float"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
        """Return a tuple"""
        return (k, float(v * v))
