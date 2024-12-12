from collections import defaultdict
from itertools import product
import sys


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        return {r + c * 1j: p for r, row in enumerate(file.readlines()) for c, p in enumerate(row.strip())}


def main(grid):
    visited, areas, perimeters, corners = set(), defaultdict(int), defaultdict(int), defaultdict(int)
    for idx, p in grid.items():
        if idx in visited:
            continue
        stack = {idx}
        while stack:
            current = stack.pop()
            visited.add(current)
            areas[idx] += 1
            perimeter = 4
            for neighbour in {current + step for step in [1, -1, 1j, -1j]} & grid.keys():
                if grid[neighbour] == p:
                    perimeter -= 1
                    if neighbour not in visited:
                        stack.add(neighbour)
            perimeters[idx] += perimeter
            for n1, n2 in [(current + d1, current + d2) for d1, d2 in product([1, -1], [1j, -1j])]:
                if (
                    (n1 in grid and n2 in grid and grid[n1] != p and grid[n2] != p)
                    or (n1 in grid and n2 in grid and grid[n1] == p and grid[n2] == p and grid[n1 + n2 - current] != p)
                    or (n1 not in grid and n2 not in grid)
                    or (n1 not in grid and grid[n2] != p)
                    or (n2 not in grid and grid[n1] != p)
                ):
                    corners[idx] += 1

    return (
        sum(area * perimeter for area, perimeter in zip(areas.values(), perimeters.values())),
        sum(area * corner for area, corner in zip(areas.values(), corners.values())),
    )


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    p1, p2 = main(inp)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
