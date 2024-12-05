#!/usr/bin/env python3

import sys
import os
import re


def parse_input(argv):
    with open(argv[1], "r") as file:
        inp = file.read()
    return inp


def sum_mults(inp):
    res = 0
    exps = re.findall("mul\(\d{1,3},\d{1,3}\)", inp)
    for exp in exps:
        n1, n2 = re.findall("\d{1,3}", exp)
        res += int(n1) * int(n2)

    return res


def part_one(inp):
    res = sum_mults(inp)

    print("Part 1")
    print(res)


def part_two(inp):
    total = 0
    while "do()" in inp:
        next_dont = inp.find("don't()")
        enabled = inp[:next_dont]

        for exp in re.findall(r"mul\(\d{1,3},\d{1,3}\)", enabled):
            n1, n2 = re.findall(r"\d{1,3}", exp)
            total += int(n1) * int(n2)

        inp = inp[next_dont:]
        next_do = inp.find("do()")
        inp = inp[next_do:]

    print("Part 2")
    print(total)


def main(inp):
    part_one(inp)
    part_two(inp)


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    main(inp)
