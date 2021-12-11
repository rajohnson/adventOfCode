class NavigationSyntax:
    def getLines(self, filename):
        lines = []
        with open(filename) as file:
            for line in file:
                lines.append(line.strip())
        return lines

    def __init__(self, filename):
        self.unsorted = self.getLines(filename)
        self.incomplete = []
        self.corrupt = []
        self.assessLines()

    def assessLines(self):
        opening = "({[<"
        closing = ")}]>"
        while self.unsorted:
            line = self.unsorted.pop()
            brackets = []
            for c in line:
                if c in opening:
                    brackets.append(c)
                else:
                    if c == closing[opening.index(brackets[-1])]:
                        brackets.pop()
                    else:
                        self.corrupt.append(c)
                        break

    def corruptScores(self):
        return sum(self.getScore(c) for c in self.corrupt)

    def getScore(self, c):
        scores = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137,
        }
        return scores[c]


if __name__ == "__main__":
    result = NavigationSyntax("input.txt").corruptScores()
    print(result)
