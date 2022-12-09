class Coordinate:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Coordinate({self.x}, {self.y})"


def update_segment(leader: Coordinate, follower: Coordinate):
    deltaX = leader.x - follower.x
    deltaY = leader.y - follower.y
    if abs(deltaX) == 2 and abs(deltaY) == 1:
        follower.x += deltaX // abs(deltaX)
        follower.y += deltaY // abs(deltaY)
    elif abs(deltaX) == 1 and abs(deltaY) == 2:
        follower.x += deltaX // abs(deltaX)
        follower.y += deltaY // abs(deltaY)
    elif abs(deltaX) == 2:
        follower.x += deltaX // abs(deltaX)
    elif abs(deltaY) == 2:
        follower.y += deltaY // abs(deltaY)
    return follower


def process_move(
    line: str, rope: list[Coordinate], visited: list[Coordinate]
) -> list[list[Coordinate], list[Coordinate]]:
    direction, num = line.split()
    for _ in range(int(num)):
        if direction == "R":
            rope[0].x += 1
        elif direction == "L":
            rope[0].x -= 1
        elif direction == "U":
            rope[0].y += 1
        elif direction == "D":
            rope[0].y -= 1
        for leader, follower in zip(rope, rope[1:]):
            update_segment(leader, follower)
        visited.add((rope[-1].x, rope[-1].y))

    return rope, visited


def part1(filename: str):
    rope = [Coordinate(0, 0), Coordinate(0, 0)]
    visited = set()
    with open(filename, "r") as file_in:
        for line in file_in:
            rope, visited = process_move(line, rope, visited)
    return len(visited)


def part2(filename: str):
    rope = [Coordinate(0, 0) for _ in range(10)]
    visited = set()
    with open(filename, "r") as file_in:
        for line in file_in:
            rope, visited = process_move(line, rope, visited)
    return len(visited)


if __name__ == "__main__":
    print(f"{part1('input.txt')=}")
    print(f"{part2('input.txt')=}")
