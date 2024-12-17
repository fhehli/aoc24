import re
import sys

from random import randint


def parse_input(argv):
    with open(argv[1] if len(sys.argv) >= 2 else "inputs/test") as file:
        register_str, program_str = file.read().split("\n\n")
    register = list(map(int, re.findall(r"(\d+)", register_str)))
    program = list(map(int, re.findall(r"(\d)", program_str)))

    return register, program


def part_one(register, program):
    register_ = [i for i in register]
    i, out = 0, ""

    def combo_op(op, register__):
        return op if op < 4 else register__[op - 4]

    while i < len(program):
        opcode, op = program[i : i + 2]
        if opcode == 0:
            register_[0] //= 2 ** combo_op(op, register_)
        elif opcode == 1:
            register_[1] ^= op
        elif opcode == 2:
            register_[1] = combo_op(op, register_) % 8
        elif opcode == 3 and register_[0]:
            i = op
            continue
        elif opcode == 4:
            register_[1] ^= register_[2]
        elif opcode == 5:
            out += f",{combo_op(op, register_) % 8}"
        elif opcode == 6:
            register_[1] = register_[0] // 2 ** combo_op(op, register_)
        elif opcode == 7:
            register_[2] = register_[0] // 2 ** combo_op(op, register_)

        i += 2

    return out[1:]


def part_two(register, program):
    def p(register_):
        A = register_[0]
        out = ""
        while A:
            out += f",{(A % 8) ^ ((A >> (7 - A % 8)) % 8)}"
            A >>= 3
        return out[1:]

    assert all(
        part_one(register_, program) == p(register_)
        for register_ in [[randint(0, 2**50) for _ in range(3)] for _ in range(100)]
    )  # p is equal to program

    candidates = [0]
    for val in reversed(program):
        new_candidates = []
        for A in candidates:
            for x in range(8):
                A_ = (A << 3) | x
                if (A_ % 8) ^ ((A_ >> (7 - A_ % 8)) % 8) == val:
                    new_candidates.append(A_)
        candidates = new_candidates

    return next(candidate for candidate in candidates if [int(i) for i in p([candidate, 0, 0]).split(",")] == program)


if __name__ == "__main__":
    inp = parse_input(sys.argv)
    print(f"Part 1: {part_one(*inp)}")
    print(f"Part 2: {part_two(*inp)}")
