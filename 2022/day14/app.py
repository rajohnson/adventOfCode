import collections
import re


Point = collections.namedtuple("Point", "x y")
point_regex = re.compile(r"(\d+),(\d+)")


def part1(filename: str):
    with open(filename, "r") as file_in:
        data = file_in.read()
    points = [
        Point(point.group(1), point.group(2))
        for point in point_regex.finditer(data)
    ]

    return (
        max(p.x for p in points),
        min(p.x for p in points),
        max(p.y for p in points),
        min(p.y for p in points),
    )


def part2(filename: str):
    return None


if __name__ == "__main__":
    print(f"{part1('example.txt')=}")
    print(f"{part2('example.txt')=}")
