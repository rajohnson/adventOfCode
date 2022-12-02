import re


def first_attempt():
    with open("input.txt", "r") as data_in:
        inventory = []
        all_inventories = []
        for line in data_in:
            if len(line) == 1:  # new elf
                all_inventories.append(inventory)
                inventory = []
            else:
                inventory.append(int(line))
        if inventory:  # last one if the file doesn't have an extra newline
            all_inventories.append(inventory)

    part1_solution = max([sum(inventory) for inventory in all_inventories])
    part2_solution = sum(sorted([sum(inventory) for inventory in all_inventories])[-3:])

    return part1_solution, part2_solution


def second_attempt():
    with open("input.txt", "r") as data_in:
        groups = re.split(r"(?:\r?\n){2,}", data_in.read())
    all_inventories = [[int(items) for items in group.split()] for group in groups]

    part1_solution = max([sum(inventory) for inventory in all_inventories])
    part2_solution = sum(sorted([sum(inventory) for inventory in all_inventories])[-3:])
    return part1_solution, part2_solution


def third_attempt():
    all_inventories = [0]
    with open("input.txt", "r") as data_in:
        for line in data_in:
            stripped = line.strip()
            if stripped:
                all_inventories[-1] += int(stripped)
            else:
                all_inventories.append(0)

        part1_solution = max(all_inventories)
        part2_solution = sum(sorted(all_inventories)[-3:])
        return part1_solution, part2_solution


def fourth_attempt():
    all_inventories = [0]
    with open("input.txt", "r") as data_in:
        for line in data_in:
            if len(line) != 1:
                all_inventories[-1] += int(line)
            else:
                all_inventories.append(0)

        part1_solution = max(all_inventories)
        part2_solution = sum(sorted(all_inventories)[-3:])
        return part1_solution, part2_solution


if __name__ == "__main__":
    import timeit

    repeats = 1000
    for index, attempt in enumerate(
        [first_attempt, second_attempt, third_attempt, fourth_attempt]
    ):
        timing = timeit.timeit(attempt, number=repeats)
        print(f"Attempt {index+1}: result = {attempt()}, timing = {timing:.3f}")
