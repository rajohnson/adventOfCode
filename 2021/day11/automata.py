import pathlib  # trying something new


class Octopuses:
    def __init__(self, filename):
        text = pathlib.Path(filename).read_text()
        self.arr = [[int(c) for c in line] for line in text.split()]
        self.flashes = 0

    def update(self, n=1):
        for _ in range(n):
            # add 1 to each square
            for y in range(len(self.arr)):
                for x in range(len(self.arr[0])):
                    self.updateSquare(1, x, y)
            # clear all flashed squares to 0
            for y in range(len(self.arr)):
                for x in range(len(self.arr[0])):
                    if self.arr[y][x] > 9:
                        self.arr[y][x] = 0

    def updateSquare(self, value, x, y):
        if 0 <= y < len(self.arr) and 0 <= x < len(
            self.arr[0]
        ):  # skip over this update if out of bounds
            if self.arr[y][x] <= 9:
                self.arr[y][x] += value
                if self.arr[y][x] > 9:
                    self.flashes += 1
                    self.updateSquare(1, x - 1, y - 1)
                    self.updateSquare(1, x, y - 1)
                    self.updateSquare(1, x + 1, y - 1)
                    self.updateSquare(1, x - 1, y)
                    self.updateSquare(1, x + 1, y)
                    self.updateSquare(1, x - 1, y + 1)
                    self.updateSquare(1, x, y + 1)
                    self.updateSquare(1, x + 1, y + 1)

    def __repr__(self):
        result = ""
        for row in self.arr:
            for value in row:
                result += str(value)
            result += "\n"
        result += f"flashes={self.flashes}"
        return result

    def updatesUntilSimultaneous(self):
        updates = 0
        flashesLast = self.flashes
        while self.flashes - flashesLast != len(self.arr) * len(self.arr[0]):
            flashesLast = self.flashes
            updates += 1
            self.update()
        return updates


if __name__ == "__main__":
    game = Octopuses("input.txt")
    print(game.updatesUntilSimultaneous())
