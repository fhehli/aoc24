#!/usr/bin/env python3

from collections import defaultdict
from graphlib import TopologicalSorter
import sys
import os


def parse_input(argv) -> tuple[defaultdict[int : set[int]], list[tuple[int]]]:
    with open(argv[1]) as file:
        rules_str, updates_str = file.read().split("\n\n")

    rules = defaultdict(set)
    for rule in rules_str.split():
        left_page, right_page = list(map(int, rule.split("|")))
        rules[left_page].add(right_page)

    updates = [tuple(map(int, update.split(","))) for update in updates_str.split()]

    return rules, updates


def correct_updates(inp) -> list[tuple[int]]:
    rules, updates = inp
    return [
        update
        for update in updates
        if all(
            current_page not in rules[next_page]
            for i, current_page in enumerate(update)
            for next_page in update[i + 1 :]
        )
    ]


def part_one(inp):
    return sum([update[len(update) // 2] for update in correct_updates(inp)])


def part_two(inp):
    rules, updates = inp
    incorrect_updates = list(set(updates) - set(correct_updates(inp)))
    total = 0
    for update in incorrect_updates:
        graph = {page: rules[page] & set(update) for page in update}
        reverse_order = list(TopologicalSorter(graph).static_order())
        total += reverse_order[len(reverse_order) // 2]

    return total


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(inp)}")
    print(f"Part 2: {part_two(inp)}")
