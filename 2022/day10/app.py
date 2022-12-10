import itertools
import collections


Status = collections.namedtuple("Status", "accumulator_delta cycles")


def cycles_for_instruction(line: str) -> int:
    if line.startswith("noop"):
        return 1
    elif line.startswith("addx"):
        return 2
    else:
        raise NotImplementedError


def accumulator_change(line: str) -> int:
    if line.startswith("noop"):
        return 0
    elif line.startswith("addx"):
        _, value = line.split()
        return int(value)
    else:
        raise NotImplementedError


def get_signal_strength(history: list[Status], cycle_of_interest: int) -> int:
    running_total, total_cycles = 1, 0  # accumulator starts at 1
    for entry in history:
        if (
            new_total_cycles := total_cycles + entry.cycles
        ) < cycle_of_interest:
            running_total += entry.accumulator_delta
            total_cycles = new_total_cycles
    return running_total * cycle_of_interest


def part1(filename: str):
    with open(filename, "r") as file_in:
        data = file_in.readlines()
    system_status = [
        Status(
            accumulator_change(instruction),
            cycles_for_instruction(instruction),
        )
        for instruction in data
    ]
    cycles_of_interest = [20 + 40 * i for i in range(6)]
    signal_strengths = [
        get_signal_strength(system_status, cycle)
        for cycle in cycles_of_interest
    ]

    return sum(signal_strengths)


def part2(filename: str):
    return None


if __name__ == "__main__":
    print(f"{part1('input.txt')=}")
    print(f"{part2('input.txt')=}")
