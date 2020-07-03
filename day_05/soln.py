with open("input.txt") as input_file:
    polymer = input_file.readline().strip()


def cancels(cur, suc):
    return cur.lower() == suc.lower() and cur != suc


def poly_reduce_one(polymer):
    for i in range(len(polymer) - 1):
        cur = polymer[i]
        suc = polymer[i + 1]
        if cancels(cur, suc):
            reduced_polymer = polymer[:i] + polymer[i + 2 :]
            return reduced_polymer
    # slow
    # polymer = [x for i, x in enumerate(polymer[:-2]) if not cancels(polymer[i], polymer[i+1])]
    return polymer


def poly_reduce(polymer):
    while len(polymer) != len(poly_reduce_one(polymer)):
        polymer = poly_reduce_one(polymer)
    return polymer


def remove_unit(polymer, unit):
    unit_removed = [x for x in polymer if x.lower() != unit.lower()]
    return "".join(unit_removed)


if __name__ == "__main__":
    # print(f"P1 Answer: {len(poly_reduce(polymer))}")

    units = list(set(map(lambda x: x.lower(), polymer)))
    unit_poly_lengths = {}

    # this slow
    for i, x in enumerate(units):
        print(
            f"Starting unit: {x}, progress: ({i} / {len(units)} total units completed)"
        )
        unit_removed = remove_unit(polymer, x)
        unit_removed = poly_reduce(unit_removed)
        unit_poly_lengths[x] = len(unit_removed)
    shortest_poly = min(unit_poly_lengths.values())
    print(f"P2 Answer: {shortest_poly}")
