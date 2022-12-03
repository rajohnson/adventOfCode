import string


def get_priority(c: str) -> int:
    priorities = string.ascii_lowercase + string.ascii_uppercase
    return priorities.index(c) + 1


def intersection_of_halves(line: str):
    half = len(line) // 2
    return set(line[:half]).intersection(set(line[half:])).pop()


def part1():
    with open("input.txt", "r") as file_in:
        data = [get_priority(intersection_of_halves(line.strip())) for line in file_in]
    return sum(data)


def find_common_item(a, b, c):
    return set(a).intersection(b).intersection(c).pop()


def part2():
    with open("input.txt", "r") as file_in:
        lines = [line.strip() for line in file_in.readlines()]
        groups = zip(lines[0::3], lines[1::3], lines[2::3])
        priority_scores = [
            get_priority(find_common_item(a, b, c)) for a, b, c in groups
        ]
    return sum(priority_scores)


if __name__ == "__main__":
    print(part1())
    print(part2())
