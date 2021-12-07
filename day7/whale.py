def align(filename):
    with open(filename) as file:
        positions = list(map(int, file.readline().split(",")))
        fuelUsed = []
        for i in range(max(positions)):
            fuelUsed.append(0)  # creates index i
            for pos in positions:
                fuelUsed[i] += abs(pos - i)
    return min(fuelUsed)


if __name__ == "__main__":
    testResult = align("test.txt")
    print(testResult)
    inputResult = align("input.txt")
    print(inputResult)
