import collections


def chars_to_unique_window(s: str, size: int) -> int:
    window = collections.deque(maxlen=size)
    count = 1
    for c in s:
        window.append(c)
        if len(set(window)) == size:  # filter out duplicates with set
            break
        count += 1
    return count


def part1(filename: str):
    with open(filename, "r") as file_in:
        data = file_in.read()
    return chars_to_unique_window(data, 4)


def part2(filename: str):
    with open(filename, "r") as file_in:
        data = file_in.read()
    return chars_to_unique_window(data, 14)


if __name__ == "__main__":
    print(f"{part1('input.txt')=}")
    print(f"{part2('input.txt')=}")
