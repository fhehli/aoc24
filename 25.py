from itertools import product
import sys

import numpy as np


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        raw = file.read().split("\n\n")
    locks, keys = (
        [x.split() for x in raw if x.startswith(".")],
        [x.split() for x in raw if x.startswith("#")],
    )
    locks = np.array([[sum(c == "#" for i in range(1, 6) for c in lock[i][j]) for j in range(5)] for lock in locks])
    keys = np.array([[sum(c == "#" for i in range(1, 6) for c in key[i][j]) for j in range(5)] for key in keys])
    return locks, keys


def part_one(locks, keys):
    return sum(all(lock + key <= 5) for lock, key in product(locks, keys))


def part_two(locks, keys):
    pass


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(*inp)}")
    print(f"Part 2: {part_two(*inp)}")
