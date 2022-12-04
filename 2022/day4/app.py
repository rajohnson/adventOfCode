def complete_overlap(a: set[int], b: set[int]) -> bool:
    return a.issubset(b) or a.issuperset(b)


def overlap(a: set[int], b: set[int]) -> bool:
    return not a.isdisjoint(b)


def coordinate_to_set(coord: str) -> set[int]:
    start, end = coord.split("-")
    return set(range(int(start), int(end) + 1))


def get_pair(line: str) -> list[set[int]]:
    return (coordinate_to_set(coord) for coord in line.strip().split(","))


def part1():
    with open("input.txt", "r") as file_in:
        complete_overlaps = [
            [get_pair(line)]
            for line in file_in.readlines()
            if complete_overlap(*get_pair(line))
        ]
    return len(complete_overlaps)


def part2():
    with open("input.txt", "r") as file_in:
        overlaps = [
            [get_pair(line)] for line in file_in.readlines() if overlap(*get_pair(line))
        ]
    return len(overlaps)


if __name__ == "__main__":
    print(f"{part1()=}")
    print(f"{part2()=}")
