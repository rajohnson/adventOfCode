class Coordinate:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Coordinate({self.x}, {self.y})"


def update_tail(head: Coordinate, tail: Coordinate):
    deltaX = head.x - tail.x
    deltaY = head.y - tail.y
    if abs(deltaX) == 2 and abs(deltaY) == 1:
        tail.x += deltaX // abs(deltaX)
        tail.y += deltaY // abs(deltaY)
    elif abs(deltaX) == 1 and abs(deltaY) == 2:
        tail.x += deltaX // abs(deltaX)
        tail.y += deltaY // abs(deltaY)
    elif abs(deltaX) == 2:
        tail.x += deltaX // abs(deltaX)
    elif abs(deltaY) == 2:
        tail.y += deltaY // abs(deltaY)
    return tail


def process_move(
    line: str, head: Coordinate, tail: Coordinate, visited: list[Coordinate]
) -> list[Coordinate, Coordinate, list[Coordinate]]:
    direction, num = line.split()
    for _ in range(int(num)):
        if direction == "R":
            head.x += 1
        elif direction == "L":
            head.x -= 1
        elif direction == "U":
            head.y += 1
        elif direction == "D":
            head.y -= 1
        tail = update_tail(head, tail)
        visited.add((tail.x, tail.y))

    return head, tail, visited


def part1(filename: str):
    head = Coordinate(0, 0)
    tail = Coordinate(0, 0)
    visited = set()
    with open(filename, "r") as file_in:
        for line in file_in:
            head, tail, visited = process_move(line, head, tail, visited)
    return len(visited)


def part2(filename: str):
    return None


if __name__ == "__main__":
    print(f"{part1('input.txt')=}")
    print(f"{part2('input.txt')=}")
