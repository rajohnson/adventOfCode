class Grid:
    def __init__(self, filename):
        with open(filename) as file:
            self.arr = [
                [int(value) for value in row.strip()] for row in file.readlines()
            ]
            self.minima = set()
            self.yMax = len(self.arr)
            self.xMax = len(self.arr[0])
            self.toTest = {(x, y) for x in range(self.xMax) for y in range(self.yMax)}
            self.run()

    def run(self):
        while self.toTest:
            self.evaluateSquare(self.toTest.pop())

    def evaluateSquare(self, square):
        x, y = square
        value = self.getRiskLevel(x, y)
        up = self.getRiskLevel(x, y - 1)
        down = self.getRiskLevel(x, y + 1)
        left = self.getRiskLevel(x - 1, y)
        right = self.getRiskLevel(x + 1, y)
        smallestAdjacent = min([up, down, left, right])
        if value < smallestAdjacent:
            self.minima.add(square)

    def __repr__(self):
        return f"{self.arr}"

    def getRiskLevel(self, x, y):
        if not 0 <= x < self.xMax or not 0 <= y < self.yMax:
            return float("inf")
        return self.arr[y][x] + 1

    def getMinimaRisks(self):
        return sum(self.getRiskLevel(x, y) for x, y in self.minima)


if __name__ == "__main__":
    result = Grid("input.txt")
    print(result.getMinimaRisks())
