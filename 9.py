import sys
import os

import numpy as np


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        disk_map = list(file.read().strip())
    disk = ["." if i % 2 else i / 2 for i, size in enumerate(disk_map) for _ in range(int(size))]
    return disk


def part_one(disk):
    left, right = 0, len(disk) - 1
    while left < right:
        while left < right and disk[left] != ".":
            left += 1
        while left < right and disk[right] == ".":
            right -= 1
        disk[left], disk[right] = disk[right], disk[left]

    return sum([i * float(x) for i, x in enumerate(disk) if x != "."])


def part_two(disk):
    fileID = disk[-1]
    while fileID > 0:
        size = sum([x == fileID for x in disk])
        p = 0
        while p < disk.index(fileID):
            while disk[p] not in [".", fileID]:
                p += 1
            empty_size = 0
            while disk[p + empty_size] == ".":
                empty_size += 1
            if size <= empty_size:
                l = disk.index(fileID)
                for i in range(size):
                    disk[p + i] = fileID
                    disk[l + i] = "."
                break
            p += empty_size
        fileID -= 1

    return sum([i * float(x) for i, x in enumerate(disk) if x != "."])


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(np.copy(inp))}")
    print(f"Part 2: {part_two(inp)}")
