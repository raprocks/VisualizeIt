"""
VisualizeIt base package
"""

__version__ = '0.1'


import random


def create_random_array(n: int):
    return [random.randint(0, 512) for _ in range(n)]
