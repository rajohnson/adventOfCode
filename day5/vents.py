import dataclasses
import re
import collections
import itertools


@dataclasses.dataclass
class Point:
    x: int
    y: int


@dataclasses.dataclass
class Line:
    start: Point
    end: Point

    @property
    def isHorizontal(self):
        return self.start.y == self.end.y

    @property
    def isVertical(self):
        return self.start.x == self.end.x

    @property
    def isDiagonal(self):
        return not (self.isVertical or self.isHorizontal)

    """ Returns a list of points that the line will pass through."""

    def points(self):
        points = []
        if self.isHorizontal:
            increment = 1 if self.start.x < self.end.x else -1
            for x in range(self.start.x, self.end.x + increment, increment):
                points.append(f"x{x}y{self.start.y}")
        elif self.isVertical:
            increment = 1 if self.start.y < self.end.y else -1
            for y in range(self.start.y, self.end.y + increment, increment):
                points.append(f"x{self.start.x}y{y}")
        else:
            yIncrement = 1 if self.start.y < self.end.y else -1
            xIncrement = 1 if self.start.x < self.end.x else -1
            for x, y in zip(
                range(self.start.x, self.end.x + xIncrement, xIncrement),
                range(self.start.y, self.end.y + yIncrement, yIncrement),
            ):
                points.append(f"x{x}y{y}")
        return points


def process(filename):
    with open(filename) as file:
        lines = []
        for line in file:
            match = re.match(
                r"(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)", line
            )
            lines.append(
                Line(
                    Point(int(match.group("x1")), int(match.group("y1"))),
                    Point(int(match.group("x2")), int(match.group("y2"))),
                )
            )
        points = collections.Counter()
        for line in lines:
            points.update(line.points())
        return len(list(itertools.takewhile(lambda i: i[1] >= 2, points.most_common())))


if __name__ == "__main__":
    print(process("input.txt"))
