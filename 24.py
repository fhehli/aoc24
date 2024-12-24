from copy import deepcopy
import sys

import networkx as nx


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        initial_states, gates = file.read().split("\n\n")
    initial_states = dict([line.split(": ") for line in initial_states.splitlines()])
    initial_states = {k: int(v) for k, v in initial_states.items()}
    gates = [line.replace("-> ", "").split() for line in gates.splitlines()]
    G = nx.from_edgelist(((gate[i], gate[-1]) for gate in gates for i in [0, 2]), create_using=nx.DiGraph)
    order = list(nx.topological_sort(G))
    gates = sorted(gates, key=lambda x: order.index(x[-1]))
    return initial_states, gates


def part_one(states, gates):
    for a, op, b, target in gates:
        match op:
            case "AND":
                states[target] = states[a] & states[b]
            case "OR":
                states[target] = states[a] | states[b]
            case "XOR":
                states[target] = states[a] ^ states[b]

    z_states = sorted([(w, str(s)) for w, s in states.items() if w.startswith("z")], reverse=True)
    return int("".join(s[1] for s in z_states), 2)


def part_two(states, gates):
    for exp in range(45):
        x, y = 2**exp, 1
        for i in range(45):
            states[f"x{i:02}"], states[f"y{i:02}"] = (x >> i) & 1, (y >> i) & 1
        if part_one(states, gates) != x + y:
            print(f"Something wrong near bit {exp}")


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(*deepcopy(inp))}")
    print(f"Part 2: {part_two(*inp)}")
