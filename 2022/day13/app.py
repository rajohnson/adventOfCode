import itertools


def read_pairs(filename: str) -> list[str]:
    with open(filename, "r") as file_in:
        data = file_in.read()
    return [pair.splitlines() for pair in data.split("\n\n")]


# return true if left side is lower, false if right side is lower, None if
# both are equal
def compare_pair(a, b):
    if a is None:
        return True
    if b is None:
        return False
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None
        return a < b
    if isinstance(a, list) and isinstance(b, list):
        for pair in itertools.zip_longest(a, b):
            # print(pair)
            if (result := compare_pair(*pair)) is not None:
                return result
        return None
    if isinstance(a, list) and isinstance(b, int):
        return compare_pair(a, [b])
    if isinstance(a, int) and isinstance(b, list):
        return compare_pair([a], b)
    raise ValueError("didn't handle case")


def part1(filename: str):
    correct_order_ndx = []
    for index, (a_str, b_str) in enumerate(read_pairs(filename)):
        a = eval(a_str)
        b = eval(b_str)
        print(index + 1)
        print(a)
        print(b)
        print(compare_pair(a, b))
        print()
        if compare_pair(a, b):
            correct_order_ndx.append(index + 1)
    return sum(correct_order_ndx)


def part2(filename: str):
    return None


if __name__ == "__main__":
    print(f"{part1('input.txt')=}")
    print(f"{part2('input.txt')=}")
