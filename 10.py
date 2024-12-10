import sys
import os

import numpy as np


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        grid = np.array([list(map(int, line.strip())) for line in file.readlines()])
    return grid


def main(grid):
    reachable_9s = {(i, j): {(i, j)} if h == 9 else set() for i, r in enumerate(grid) for j, h in enumerate(r)}
    ratings = {(i, j): 1 if h == 9 else 0 for i, r in enumerate(grid) for j, h in enumerate(r)}
    for h in range(8, -1, -1):
        for loc in np.argwhere(grid == h):
            for neighbour in loc + np.array([[1, 0], [-1, 0], [0, 1], [0, -1]]):
                if tuple(neighbour) in reachable_9s and grid[*neighbour] == grid[*loc] + 1:
                    reachable_9s[tuple(loc)] |= reachable_9s[tuple(neighbour)]
                    ratings[tuple(loc)] += ratings[tuple(neighbour)]

    return (
        sum([len(reachable_9s[tuple(loc)]) for loc in np.argwhere(grid == 0)]),
        sum([ratings[tuple(loc)] for loc in np.argwhere(grid == 0)]),
    )


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    p1, p2 = main(inp)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
