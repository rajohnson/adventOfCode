import dataclasses
import collections
from typing import Callable


@dataclasses.dataclass
class Point:
    x: int
    y: int
    height: int
    distance: int | None = None


# return the start, end, and a nested list of Points representing the grid
def create_grid(filename: str) -> tuple[Point, Point, list[list[Point]]]:
    with open(filename, "r") as file_in:
        data = file_in.read()
    start, end = None, None
    grid = []
    for y, line in enumerate(data.splitlines()):
        row = []
        for x, value in enumerate(line):
            if value == "S":
                start = Point(x, y, ord("a"))
                row.append(start)
            elif value == "E":
                end = Point(x, y, ord("z"))
                row.append(end)
            else:
                row.append(Point(x, y, ord(value)))
        grid.append(row)

    if start is None or end is None:
        raise ValueError("didn't assign start or end")
    return start, end, grid


def neighbor_navigable(
    point: Point, x: int, y: int, grid: list[list[Point]]
) -> bool:
    max_x = len(grid[0])
    max_y = len(grid)
    if (0 <= x < max_x) and (0 <= y < max_y):
        if grid[y][x].distance is None:
            if (grid[y][x].height - point.height) >= -1:
                return True
    return False


def render_distance(grid: list[list[Point]]) -> None:
    print()
    for row in grid:
        print(
            "".join(
                str(point.distance % 10)
                if point.distance is not None
                else chr(point.height)
                for point in row
            )
        )


# return the length of the shortest path from end to start
def bfs(
    is_target: Callable[[Point], bool],
    end: Point,
    grid: list[list[Point]],
    debug: bool = False,
) -> int:
    path_queue = collections.deque([end])
    end.distance = 0
    while path_queue:
        current = path_queue.popleft()
        if current.distance is None:
            raise ValueError("distance was not assigned")
        if is_target(current):
            if current.distance is None:
                raise ValueError("distance was not set.")
            return current.distance
        possible_neighbors = [
            (current.x - 1, current.y),
            (current.x + 1, current.y),
            (current.x, current.y - 1),
            (current.x, current.y + 1),
        ]
        for neighbor_coords in possible_neighbors:
            neighbor_x, neighbor_y = neighbor_coords
            if neighbor_navigable(current, neighbor_x, neighbor_y, grid):
                neighbor = grid[neighbor_y][neighbor_x]
                neighbor.distance = current.distance + 1
                path_queue.append(neighbor)
        if debug:
            render_distance(grid)

    raise ValueError("search didn't reach goal")


def part1(filename: str) -> int:
    start, end, grid = create_grid(filename)
    return bfs(lambda x: x is start, end, grid)


def part2(filename: str):
    return None


if __name__ == "__main__":
    print(f"{part1('example.txt')=}")
    print(f"{part1('input.txt')=}")
    print(f"{part2('input.txt')=}")
