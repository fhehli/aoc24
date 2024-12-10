from itertools import combinations
from string import ascii_letters
import sys
import os

import numpy as np


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        grid = np.array(list(map(list, file.read().split())))
    return grid


def part_one(grid):
    antinodes = {(i, j): 0 for i, row in enumerate(grid) for j, c in enumerate(row)}
    for c in list(ascii_letters) + [str(i) for i in range(10)]:
        nodes = np.argwhere(grid == c)
        if not len(nodes):
            continue
        for n1, n2 in combinations(nodes, r=2):
            if (loc := tuple(2 * n1 - n2)) in antinodes:
                antinodes[loc] = 1
            if (loc := tuple(2 * n2 - n1)) in antinodes:
                antinodes[loc] = 1

    return sum(antinodes.values())


def part_two(grid):
    antinodes = {(i, j): 0 for i, row in enumerate(grid) for j, c in enumerate(row)}
    for c in list(ascii_letters) + [str(i) for i in range(10)]:
        nodes = np.argwhere(grid == c)
        if not len(nodes):
            continue
        for n1, n2 in combinations(nodes, r=2):
            for sgn in [-1, 1]:
                d = sgn * (n1 - n2)
                loc = (1 + sgn) / 2 * n1 - (-1 + sgn) / 2 * n2
                while tuple(loc) in antinodes:
                    antinodes[tuple(loc)] = 1
                    loc += d

    return sum(antinodes.values())


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(np.copy(inp))}")
    print(f"Part 2: {part_two(inp)}")
