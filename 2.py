#!/usr/bin/env python3

import sys
import os


def parse_input(args):
    return args[1]


def is_safe(line: list) -> int:
    for i in range(len(line) - 1):
        if not line[i] < line[i + 1] < line[i] + 4:
            return 0
    return 1


def part_one(inp):
    counter = 0
    with open(inp, "r") as f:
        for line in f:
            line_list = [int(i) for i in line.strip().split()]
            counter += is_safe(line_list) or is_safe(line_list[::-1])

    print("Part 1:", counter)


def is_safe2(line: list) -> int:
    have_removed = False
    skip_next = False
    for i in range(len(line) - 1):
        if skip_next:
            skip_next = False
            continue
        if not line[i] < line[i + 1] < line[i] + 4:
            if not have_removed and (i + 2 == len(line) or line[i] < line[i + 2] < line[i] + 4):
                have_removed = True
                skip_next = True
            else:
                return 0
    return 1


def part_two(inp):
    counter = 0
    with open(inp, "r") as f:
        for line in f:
            line_list = [int(i) for i in line.strip().split()]
            counter += (
                is_safe2(line_list)
                or is_safe(line_list[1:])
                or is_safe2(line_list[::-1])
                or is_safe(line_list[::-1][1:])
            )

    print("Part 2:", counter)


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    part_one(inp)
    part_two(inp)
