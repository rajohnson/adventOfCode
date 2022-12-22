import collections


Entry = collections.namedtuple("Entry", "value id")
MULTIPLIER = 811589153
ROUNDS = 10


def part1(filename: str):
    with open(filename, "r") as file_in:
        data = [Entry(int(num), id) for id, num in enumerate(file_in.readlines())]
        id_queue = data.copy()
    for entry in id_queue:
        index = data.index(entry)
        data.pop(index)
        while index + entry.value < 0:
            index += len(data)
        insert_index = (index + entry.value) % len(data)
        data.insert(insert_index, entry)
    obj0 = [obj for obj in data if obj.value == 0].pop()
    index0 = data.index(obj0)
    index1000 = (index0 + 1000) % len(data)
    index2000 = (index0 + 2000) % len(data)
    index3000 = (index0 + 3000) % len(data)
    return sum([data[index1000].value, data[index2000].value, data[index3000].value])


def part2(filename: str):
    with open(filename, "r") as file_in:
        data = [
            Entry(int(num) * MULTIPLIER, id)
            for id, num in enumerate(file_in.readlines())
        ]
        id_queue = data.copy()
    for _ in range(ROUNDS):  # more rounds of mixing
        for entry in id_queue:
            index = data.index(entry)
            data.pop(index)
            while index + entry.value < 0:
                index += 10_000_000 * len(data)
            insert_index = (index + entry.value) % len(data)
            data.insert(insert_index, entry)
    obj0 = [obj for obj in data if obj.value == 0].pop()
    index0 = data.index(obj0)
    index1000 = (index0 + 1000) % len(data)
    index2000 = (index0 + 2000) % len(data)
    index3000 = (index0 + 3000) % len(data)
    return sum([data[index1000].value, data[index2000].value, data[index3000].value])


if __name__ == "__main__":
    print(f"{part1('example.txt')=}")
    print(f"{part1('input.txt')=}")
    print(f"{part2('example.txt')=}")
    print(f"{part2('input.txt')=}")
