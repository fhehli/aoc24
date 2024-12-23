import sys

import networkx as nx


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        return nx.from_edgelist([set(line.split("-")) for line in file.read().splitlines()])


def part_one(G):
    return sum(
        1 for clique in nx.enumerate_all_cliques(G) if len(clique) == 3 and any(node.startswith("t") for node in clique)
    )


def part_two(G):
    return ",".join(sorted(nx.approximation.max_clique(G)))


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(inp)}")
    print(f"Part 2: {part_two(inp)}")
