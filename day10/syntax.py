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
                        brackets = []
                        break
            if brackets:
                completion = []
                while brackets:
                    completion.append(closing[opening.index(brackets.pop())])
                self.incomplete.append(completion)

    def corruptScores(self):
        return sum(self.getCorruptScore(c) for c in self.corrupt)

    def getCorruptScore(self, c):
        scores = {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137,
        }
        return scores[c]

    def completionScores(self):
        center = (
            len(self.incomplete) // 2
        )  # because of 0 indexing this is the center index
        return sorted(
            [self.getCompletionScore(completion) for completion in self.incomplete]
        )[center]

    def getCompletionScore(self, line):
        scores = {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4,
        }
        score = 0
        for c in line:
            score *= 5
            score += scores[c]
        return score


if __name__ == "__main__":
    result = NavigationSyntax("input.txt").completionScores()
    print(result)
