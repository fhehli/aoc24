import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    l, r = [], []
    with open(filename, "r") as file:
        for line in file:
            values = line.strip().split()
            l.append(int(values[0]))
            r.append(int(values[1]))
    l.sort()
    r.sort()

    print("Part 1:", sum([abs(r[i] - l[i]) for i in range(len(l))]))

    from collections import Counter

    r_counter = Counter(r)

    print("Part 2:", sum([i * r_counter[i] for i in l]))
