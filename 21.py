from itertools import permutations
from functools import cache
import sys

import numpy as np


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        return file.read().split()


def main(codes, n_robots):
    numeric_keypad = {c: i // 3 + (i % 3) * 1j for i, c in enumerate("789456123 0A") if c != " "}
    dir_keypad = {c: i // 3 + (i % 3) * 1j for i, c in enumerate(" ^A<v>") if c != " "}
    c_to_step = {"v": 1, "^": -1, ">": 1j, "<": -1j}

    @cache
    def f(seq, depth):
        keypad = dir_keypad if depth else numeric_keypad
        loc, ans = keypad["A"], 0
        for c in seq:
            d = keypad[c] - loc
            paths = {
                path + "A"
                for path in set(
                    "".join(path)
                    for path in permutations(
                        (
                            (int(d.real) * "v" if d.real > 0 else -int(d.real) * "^")
                            + (int(d.imag) * ">" if d.imag > 0 else -int(d.imag) * "<")
                        )
                    )
                )
                if all(loc_ in keypad.values() for loc_ in np.cumsum([loc] + [c_to_step[c] for c in path]))
            }
            loc = keypad[c]
            ans += min(f(path, depth + 1) for path in paths) if depth < n_robots else abs(d.real) + abs(d.imag) + 1

        return int(ans)

    return sum(int(code[:-1]) * f(code, 0) for code in codes)


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {main(inp, 2)}")
    print(f"Part 2: {main(inp, 25)}")
