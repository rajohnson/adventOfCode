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

    def countPossiblePaths(self):
        return self.pathsToStart("end", set())

    def pathsToStart(self, location, visited):
        if location == "start":
            print(visited)
            return 1
        remainingConnections = [
            nextLocation
            for nextLocation in self.caves[location]
            if nextLocation.isupper() or nextLocation not in visited
        ]
        if not remainingConnections:
            return 0
        else:
            visited.add(location)
            ways = [
                self.pathsToStart(nextLocation, visited)
                for nextLocation in remainingConnections
            ]
            return sum(ways)


if __name__ == "__main__":
    result = Caves("test.txt").countPossiblePaths()
    print(result)
