import pathlib


class Caves:
    def __init__(self, filename):
        path = pathlib.Path(filename)
        data = path.read_text()
        pairs = [pair.split("-") for pair in data.splitlines()]

        nodeNames = set([node for pair in pairs for node in pair])
        self.caves = {name: set() for name in nodeNames}

        for a, b in pairs:
            self.caves[a].add(b)
            self.caves[b].add(a)

    def countPossiblePaths(self, extraVisitAllowed=False):
        return self.pathsToStart("end", [], extraVisitAllowed)

    def pathsToStart(self, location, visited, extraVisitAllowed):
        if location == "start":
            return 1
        extraVisitAllowedForNext = extraVisitAllowed and (
            location.isupper() or location not in visited
        )
        remainingConnections = [
            nextLocation
            for nextLocation in self.caves[location]
            if nextLocation != "end"
            and (
                nextLocation.isupper()
                or nextLocation not in visited
                or extraVisitAllowedForNext
            )
        ]
        if not remainingConnections:
            return 0
        else:
            return sum(
                self.pathsToStart(
                    nextLocation,
                    visited + [location],
                    extraVisitAllowedForNext,
                )
                for nextLocation in remainingConnections
            )


if __name__ == "__main__":
    result = Caves("test.txt").countPossiblePaths(extraVisitAllowed=True)
    print(result, 36)
    result2 = Caves("test2.txt").countPossiblePaths(extraVisitAllowed=True)
    print(result2, 103)
    result3 = Caves("test3.txt").countPossiblePaths(extraVisitAllowed=True)
    print(result3, 3509)
    result4 = Caves("test4.txt").countPossiblePaths(extraVisitAllowed=True)
    print(result4, 13)
    result5 = Caves("input.txt").countPossiblePaths(extraVisitAllowed=True)
    print(result5)
