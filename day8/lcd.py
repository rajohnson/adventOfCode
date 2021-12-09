def countUniques(filename):
    uniqueDigits = ["cf", "bcdf", "acf", "abcdefg"]
    with open(filename) as file:
        allSignals, allOutputs = [], []
        for line in file:
            signals, outputs = line.split("|")
            allSignals.append(signals)
            allOutputs.append(outputs)
        uniqueCount = 0
        uniqueLens = set(len(digit) for digit in uniqueDigits)
        for output in allOutputs:
            for outputChar in output.split():
                if len(outputChar) in uniqueLens:
                    uniqueCount += 1
    return uniqueCount


if __name__ == "__main__":
    result = countUniques("test.txt")
    print(result)

    result2 = countUniques("test2.txt")
    print(result2)

    result3 = countUniques("input.txt")
    print(result3)
