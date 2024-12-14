import re
import sys

import numpy as np


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        return [map(int, l) for line in file.readlines() for l in re.findall(r"=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)]


def part_one(robots):
    grid = np.zeros((101, 103))
    for px, py, vx, vy in robots:
        grid[(px + 100 * vx) % 101, (py + 100 * vy) % 103] += 1

    return np.prod(
        [
            np.sum(grid[: grid.shape[0] // 2, : grid.shape[1] // 2]),
            np.sum(grid[: grid.shape[0] // 2, grid.shape[1] // 2 + 1 :]),
            np.sum(grid[grid.shape[0] // 2 + 1 :, : grid.shape[1] // 2]),
            np.sum(grid[grid.shape[0] // 2 + 1 :, grid.shape[1] // 2 + 1 :]),
        ]
    )


def part_two(robots):
    pass


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(inp)}")
    print(f"Part 2: {part_two(inp)}")
