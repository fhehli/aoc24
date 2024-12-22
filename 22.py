from collections import defaultdict
import sys

import numpy as np
import scipy as sp


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        return [int(line.strip()) for line in file]


def part_one(inp):
    def simulate(n, steps):
        for _ in range(steps):
            n = (n ^ (n * 64)) % 16777216
            n = (n ^ (n // 32)) % 16777216
            n = (n ^ (n * 2048)) % 16777216
        return n

    return sum(simulate(n, 2000) for n in inp)


def part_two(inp):
    X = np.empty((len(inp), 2001), dtype=int)
    X[:, 0] = inp
    for i in range(1, 2001):
        X[:, i] = (X[:, i - 1] ^ (X[:, i - 1] * 64)) % 16777216
        X[:, i] = (X[:, i] ^ (X[:, i] // 32)) % 16777216
        X[:, i] = (X[:, i] ^ (X[:, i] * 2048)) % 16777216
    X %= 10
    D = sp.signal.convolve(X, np.array([[1, -1]]), mode="valid")
    sums = defaultdict(int)
    for i in range(X.shape[0]):
        seen = set()
        for j in range(2001 - 4):
            t = tuple(D[i, j : j + 4])
            if t not in seen:
                sums[t] += X[i, j + 4]
                seen.add(t)

    return max(sums.values())


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(inp)}")
    print(f"Part 2: {part_two(inp)}")
