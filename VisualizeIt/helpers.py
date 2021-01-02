from typing import List
import random


def create_random_array(n: int) -> List:
    return [random.randint(0, 512) for _ in range(n)]


def str_to_arr(s: str) -> List:
    return list(map(str, s.strip().split(' ')))
