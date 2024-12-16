from collections import defaultdict
from heapq import heappush, heappop
from itertools import product
import sys

import networkx as nx


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        raw = file.read()
    return {i + j * 1j: c for i, row in enumerate(raw.split()) for j, c in enumerate(row) if c != "#"}


def part_one(grid):
    start, end = next(pos for pos in grid if grid[pos] == "S"), next(pos for pos in grid if grid[pos] == "E")
    rho, heap = defaultdict(lambda: float("inf")), []
    rho[start, 1j] = 0
    heappush(heap, (0, i := 0, start, 1j))
    while heap:
        rho_, _, loc, d = heappop(heap)
        if loc + d in grid and rho[loc + d, d] > rho_ + 1:
            rho[loc + d, d] = rho_ + 1
            heappush(heap, (rho[loc + d, d], i := i + 1, loc + d, d))
        if rho[loc, 1j * d] > rho_ + 1_000:
            rho[loc, 1j * d] = rho_ + 1_000
            heappush(heap, (rho[loc, 1j * d], i := i + 1, loc, 1j * d))
        if rho[loc, -1j * d] > rho_ + 1_000:
            rho[loc, -1j * d] = rho_ + 1_000
            heappush(heap, (rho_ + 1_000, i := i + 1, loc, -1j * d))

    return min(rho[loc, d] for loc, d in rho if loc == end)


def part_two(grid):
    G = nx.DiGraph()
    for loc, d in product(grid.keys(), [1, -1, 1j, -1j]):
        if loc + d in grid:
            G.add_edge((loc, d), (loc + d, d), weight=1)
        G.add_edge((loc, d), (loc, 1j * d), weight=1_000)
        G.add_edge((loc, d), (loc, -1j * d), weight=1_000)
    start, end = next(pos for pos in grid if grid[pos] == "S"), next(pos for pos in grid if grid[pos] == "E")

    return len({loc for path in nx.all_shortest_paths(G, (start, 1j), (end, -1), weight="weight") for loc, _ in path})


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(inp)}")
    print(f"Part 2: {part_two(inp)}")
