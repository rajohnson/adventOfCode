import collections


# Finds the number of chars that have to be sampled before the window has all unique
# values. This includes the characters needed to fill the window.
# chars_to_unique_window('aaabb', 2) = 4
# If no window exists the function will return None.
def chars_to_unique_window(s: str, window_size: int) -> int:
    window = collections.deque(maxlen=window_size)
    count = 1
    for c in s:
        window.append(c)
        if len(set(window)) == window_size:  # filter out duplicates with set
            return count
        count += 1
    return None


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
