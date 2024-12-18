import copy
from itertools import product
import sys

import networkx as nx


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        positions = [complex(xy.replace(",", "+") + "j") for xy in file.read().split("\n")]
    G = nx.Graph()
    for p, d in product((grid := {i + j * 1j for i, j in product(range(71), repeat=2)}), [1, -1, 1j, -1j]):
        if p + d in grid:
            G.add_edge(p, p + d)

    return G, positions


def part_one(G, positions):
    for p in positions[:1024]:
        G.remove_node(p)

    return nx.shortest_path_length(G, 0, 70 + 70j)


def part_two(G, positions):
    for p in positions:
        G.remove_node(p)
        if 70 + 70j not in nx.node_connected_component(G, 0):
            return p


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    inp2 = copy.deepcopy(inp)
    print(f"Part 1: {part_one(*inp)}")
    print(f"Part 2: {part_two(*inp2)}")
