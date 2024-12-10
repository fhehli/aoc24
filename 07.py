import sys
import os


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        lines = [line.replace(":", "").split() for line in file.readlines()]
        lines = [[int(c) for c in line] for line in lines]
    return lines


def part_one(inp):
    total = 0
    for target, *numbers in inp:
        n = len(numbers)
        for configuration in range(2 ** (n - 1)):
            res = target
            for i in range(n):
                if not res.is_integer() or res < 0:
                    break
                if configuration >> i & 1:  # check if ith bit is one
                    res /= numbers[n - i - 1]
                else:
                    res -= numbers[n - i - 1]
            if res == 0:
                total += target
                break

    return total


def part_two(inp):
    add = lambda x, y: x + y
    multiply = lambda x, y: x * y
    concatenate = lambda x, y: int(str(x) + str(y))

    total = 0
    for target, n, *numbers in inp:
        leafs = [n]
        for y in numbers:
            leafs = [op(x, y) for x in leafs for op in [add, multiply, concatenate]]
        if target in leafs:
            total += target

    return total


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(inp)}")
    print(f"Part 2: {part_two(inp)}")
