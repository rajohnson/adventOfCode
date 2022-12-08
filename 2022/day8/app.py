from typing import List
import dataclasses
import itertools


@dataclasses.dataclass
class Tree:
    height: int
    visible: bool = False
    score: int = 0


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


# finds the score for a tree given a view (index 0 is closest) and height
def score(trees: List[Tree], height: int) -> int:
    count = 0
    for tree in trees:
        count += 1
        if tree.height >= height:
            break
    return count


def set_scores(grid: List[List[Tree]]) -> None:
    flipped_grid = list(zip(*grid))
    for x, row in enumerate(grid):
        for y, tree in enumerate(row):
            if (
                x == 0
                or x == len(row) - 1
                or y == 0
                or y == len(flipped_grid[0]) - 1
            ):
                tree.score = 0
                continue
            left = score((reversed(row[:y])), tree.height)
            right = score(row[y + 1 :], tree.height)
            up = score(list(reversed(flipped_grid[y][:x])), tree.height)
            down = score(flipped_grid[y][x + 1 :], tree.height)
            tree.score = left * right * up * down


def part1(filename: str):
    grid = build_grid(filename)
    set_visibility(grid)
    return len([tree for tree in itertools.chain(*grid) if tree.visible])


def part2(filename: str):
    grid = build_grid(filename)
    set_scores(grid)
    return max([tree.score for tree in itertools.chain(*grid)])


if __name__ == "__main__":
    print(f"{part1('input.txt')=}")
    print(f"{part2('input.txt')=}")
