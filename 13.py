import sys
import re

import numpy as np


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        machines = file.read().split("\n\n")
    return [
        [
            np.array([i, j], dtype=int)
            for line in machine.split("\n")
            for i, j in re.findall(r": X[+=](\d+), Y[+=](\d+)", line)
        ]
        for machine in machines
    ]


def main(machines, part_two=False):
    total = 0
    for A, B, prize in machines:
        prize += 10000000000000 if part_two else 0
        presses = np.linalg.solve(np.array([A, B]).T, prize).round()
        if all(np.array([A, B]).T @ presses == prize):
            total += 3 * presses[0] + presses[1]

    return int(total)


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {main(inp)}")
    print(f"Part 2: {main(inp, part_two=True)}")
