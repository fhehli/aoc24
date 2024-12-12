from collections import Counter, defaultdict
import sys


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        return [int(i) for i in file.read().strip().split()]


def part_one(stones):
    for _ in range(25):
        i, c, n_stones = 0, 0, len(stones)
        while c < n_stones:
            digits, n_digits = str(stones[i]), len(str(stones[i]))
            if stones[i] == 0:
                stones[i] = 1
                i += 1
            elif n_digits % 2 == 0:
                stones[i] = int(digits[: n_digits // 2])
                stones.insert(i + 1, int(digits[n_digits // 2 :]))
                i += 2
            else:
                stones[i] *= 2024
                i += 1
            c += 1

    return len(stones)


def part_two(stones):
    old, new = Counter(stones), defaultdict(int)
    for _ in range(75):
        new[1] += old[0]
        for key in old.keys():
            if len(str(key)) % 2 == 0:
                digits = str(key)
                new[int(digits[: len(digits) // 2])] += old[key]
                new[int(digits[len(digits) // 2 :])] += old[key]
            elif key != 0:
                new[2024 * key] += old[key]
        old, new = new, defaultdict(int)

    return sum(old.values())


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 2: {part_two(inp)}")
    print(f"Part 1: {part_one(inp)}")
