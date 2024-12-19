import functools
import sys


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        towels, designs = file.read().split("\n\n")
    towels = towels.split(", ")
    designs = designs.strip().split("\n")
    return towels, designs


def part_one(towels, designs):
    @functools.lru_cache
    def is_possible(design):
        if not design:
            return True
        return any(design.startswith(towel) and is_possible(design[len(towel) :]) for towel in towels)

    return sum(is_possible(design) for design in designs)


def part_two(towels, designs):
    @functools.lru_cache
    def n_possible(design):
        if not design:
            return True
        return sum(design.startswith(towel) and n_possible(design[len(towel) :]) for towel in towels)

    return sum(n_possible(design) for design in designs)


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(*inp)}")
    print(f"Part 2: {part_two(*inp)}")
