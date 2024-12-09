import sys
import os

import numpy as np


def parse_input(argv):
    with open(argv[1]) as file:
        grid = np.array(list(map(list, file.read().split())), dtype="<U5")
    return grid


def part_one(grid):
    current_idx = np.argwhere(grid == "^").squeeze()
    grid[*current_idx] = "X"
    direction = np.array([-1, 0])
    while True:
        next_idx = current_idx + direction
        if any(i < 0 or i >= dim_size for i, dim_size in zip(next_idx, grid.shape)):
            return np.sum(grid == "X")
        if grid[*next_idx] == "#":
            direction = np.array([direction[1], -direction[0]])
            continue
        current_idx = next_idx
        grid[*current_idx] = "X"


def check_for_loop(current_idx, direction, grid):
    grid = np.copy(grid)
    grid[*(current_idx + direction)] = "O"
    while True:
        next_idx = current_idx + direction
        if any(i < 0 or i >= dim_size for i, dim_size in zip(next_idx, grid.shape)):
            return False
        if grid[*next_idx] in ["#", "O"]:
            direction = np.array([direction[1], -direction[0]])
            continue
        if (
            ("u" in grid[*next_idx] and direction[0] < 0)
            or ("d" in grid[*next_idx] and direction[0] > 0)
            or ("l" in grid[*next_idx] and direction[1] < 0)
            or ("r" in grid[*next_idx] and direction[1] > 0)
        ):
            return True
        current_idx = next_idx
        if direction[0] < 0:
            grid[*current_idx] += "u"
        elif direction[0] > 0:
            grid[*current_idx] += "d"
        elif direction[1] < 0:
            grid[*current_idx] += "l"
        elif direction[1] > 0:
            grid[*current_idx] += "r"


def part_two(grid):
    current_idx = np.argwhere(grid == "^").squeeze()
    grid[*current_idx] = "u"
    direction = np.array([-1, 0])
    n_loops = 0
    used_fields = np.zeros_like(grid)
    while True:
        next_idx = current_idx + direction
        if any(i < 0 or i >= dim_size for i, dim_size in zip(next_idx, grid.shape)):
            return n_loops
        if grid[*next_idx] == "#":
            direction = np.array([direction[1], -direction[0]])
            continue
        if not used_fields[*next_idx]:
            loop = check_for_loop(current_idx, direction, grid)
            n_loops += loop
            used_fields[*next_idx] = loop
        current_idx = next_idx

        if direction[0] < 0:
            grid[*current_idx] += "u"
        elif direction[0] > 0:
            grid[*current_idx] += "d"
        elif direction[1] < 0:
            grid[*current_idx] += "l"
        elif direction[1] > 0:
            grid[*current_idx] += "r"


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(np.copy(inp))}")
    print(f"Part 2: {part_two(inp)}")
