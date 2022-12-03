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


if __name__ == "__main__":
    print(part1())
