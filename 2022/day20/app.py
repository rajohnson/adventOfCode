import collections


Entry = collections.namedtuple("Entry", "value id")


def part1(filename: str):
    with open(filename, "r") as file_in:
        data = [Entry(int(num), id) for id, num in enumerate(file_in.readlines())]
    # for id in range(len(data)):
    for id in range(1):
        ...
    return [d.id for d in data]


def part2(filename: str):
    return None


if __name__ == "__main__":
    print(f"{part1('example.txt')=}")
    print(f"{part2('example.txt')=}")
