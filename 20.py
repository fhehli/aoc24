from itertools import product
import sys

import networkx as nx


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        grid = {i + j * 1j: c for i, row in enumerate(file.read().split()) for j, c in enumerate(row)}
    G, H = nx.Graph(), nx.Graph()
    for loc, d in product(grid, [1, -1, 1j, -1j]):
        if grid[loc] != "#" and loc + d in grid and grid[loc + d] != "#":
            G.add_edge(loc, loc + d)
        if loc + d in grid:
            H.add_edge(loc, loc + d)
    return grid, G, H


def main(grid, G, H, start, end, cheat_length):
    start, end = next(loc for loc in grid if grid[loc] == "S"), next(loc for loc in grid if grid[loc] == "E")
    D_G = dict(nx.all_pairs_shortest_path_length(G))
    D_G[end][end] = 0

    return sum(
        D_G[start][shortcut_start] + d - 1 + D_G[shortcut_end][end] <= D_G[start][end] - 100
        for shortcut_start in G.nodes
        for shortcut_end, d in nx.single_source_shortest_path_length(H, shortcut_start, cutoff=cheat_length).items()
        if shortcut_end in G.nodes
    )


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {main(*inp, cheat_length=2)}")
    print(f"Part 2: {main(*inp, cheat_length=20)}")
