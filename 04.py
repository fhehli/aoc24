#!/usr/bin/env python3

from collections import Counter
from itertools import product
import sys
import os

import numpy as np


def parse_input(args) -> np.ndarray:
    with open(args[1], "r") as file:
        inp = np.array(list(map(list, file.read().split())))
    return inp


def part_one(inp: np.ndarray) -> int:
    return sum(
        inp[i + istep, j + jstep] == "M"
        and inp[i + 2 * istep, j + 2 * jstep] == "A"
        and inp[i + 3 * istep, j + 3 * jstep] == "S"
        for i in range(inp.shape[0])
        for j in range(inp.shape[1])
        if inp[i, j] == "X"
        for istep, jstep in product([0, 1, -1], [0, 1, -1])
        if 0 <= i + 3 * istep < inp.shape[0] and 0 <= j + 3 * jstep < inp.shape[1]
    )


def part_two(inp: np.ndarray) -> int:
    count = 0
    for i in range(1, inp.shape[0] - 1):
        for j in range(1, inp.shape[1] - 1):
            if inp[i, j] != "A":
                continue
            c = Counter([inp[i + istep, j + jstep] for istep, jstep in product([1, -1], [1, -1])])
            count += c["M"] == 2 and c["S"] == 2 and inp[i - 1, j - 1] != inp[i + 1, j + 1]

    return count


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(inp)}")
    print(f"Part 2: {part_two(inp)}")
