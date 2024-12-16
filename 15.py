import sys


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        grid, moves = file.read().split("\n\n")
    grid = {i + j * 1j: c for i, row in enumerate(grid.split()) for j, c in enumerate(row)}
    moves = [{"v": 1, "^": -1, ">": 1j, "<": -1j}[move] for move in moves.replace("\n", "")]

    return grid, moves


def part_one(grid, moves):
    pos = next(pos for pos in grid if grid[pos] == "@")
    for move in moves:
        next_pos = pos + move
        if grid[next_pos] == ".":
            grid[pos], grid[next_pos] = ".", "@"
            pos = next_pos
        elif grid[next_pos] == "O":
            d = 0
            while grid[next_pos + d] == "O":
                d += move
            if grid[next_pos + d] == ".":
                grid[pos], grid[next_pos], grid[next_pos + d] = ".", "@", "O"
                pos = next_pos

    return int(sum([100 * pos.real + pos.imag for pos, c in grid.items() if c == "O"]))


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(*inp)}")
