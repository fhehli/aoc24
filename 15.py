from copy import deepcopy
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


def part_two(grid, moves):
    boxes, walls = set(), set()
    for p, c in grid.items():
        if c == "#":
            walls.add(p.real + p.imag * 2j)
            walls.add(p.real + p.imag * 2j + 1j)
        elif c == "O":
            boxes.add(p.real + p.imag * 2j)
        elif c == "@":
            pos = p.real + p.imag * 2j

    for move in moves:
        if move.imag < 0:
            n_boxes = 0
            while pos - (n_boxes + 1) * 2j in boxes:
                n_boxes += 1
            if pos - n_boxes * 2j - 1j in walls:
                continue
            for i in range(n_boxes):
                boxes.remove(pos - (i + 1) * 2j)
                boxes.add(pos - (i + 1) * 2j - 1j)
        elif move.imag > 0:
            n_boxes = 0
            while pos + n_boxes * 2j + 1j in boxes:
                n_boxes += 1
            if pos + n_boxes * 2j + 1j in walls:
                continue
            for i in range(n_boxes):
                boxes.remove(pos + i * 2j + 1j)
                boxes.add(pos + (i + 1) * 2j)
        else:
            if pos + move in walls:
                continue
            stack = set()
            row = boxes & {pos + move - 1j, pos + move}
            while row:
                stack |= row
                new_row = boxes & {pos + move + i for pos in row for i in [-1j, 0, 1j]}
                row = new_row
            if any(p + move in walls or p + move + 1j in walls for p in stack):
                continue
            for p in stack:
                boxes.remove(p)
            for p in stack:
                boxes.add(p + move)
        pos += move

    return sum(100 * pos.real + pos.imag for pos in boxes)


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(*deepcopy(inp))}")
    print(f"Part 2: {part_two(*inp)}")
