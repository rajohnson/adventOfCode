from typing import List
import dataclasses
import itertools


@dataclasses.dataclass
class Tree:
    height: int
    visible: bool = False


def build_grid(filename: str) -> List[List[Tree]]:
    with open(filename, "r") as file_in:
        data = file_in.read()
    return [
        [Tree(int(height)) for height in line] for line in data.splitlines()
    ]


def set_visibility_line(line: List[Tree]) -> None:
    highest = line[0].height
    line[0].visible = True
    for tree in line:
        if tree.height > highest:
            tree.visible = True
            highest = tree.height


def set_visibility(grid: List[List[Tree]]) -> None:
    for row in grid:
        set_visibility_line(row)
        set_visibility_line(row[::-1])
    for col in zip(*grid):
        set_visibility_line(col)
        set_visibility_line(col[::-1])


def part1(filename: str):
    grid = build_grid(filename)
    set_visibility(grid)
    return len([tree for tree in itertools.chain(*grid) if tree.visible])


def part2(filename: str):
    return None


if __name__ == "__main__":
    print(f"{part1('input.txt')=}")
    print(f"{part2('input.txt')=}")
