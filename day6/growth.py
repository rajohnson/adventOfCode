import dataclasses


@dataclasses.dataclass
class Fish:
    cycleTime: int
    firstCycleExtraTime: int
    timeToNext: int

    def update(self):
        self.timeToNext -= 1
        if self.timeToNext < 0:
            self.timeToNext = self.cycleTime
            return Fish(
                self.cycleTime,
                timeToNext=self.cycleTime + self.firstCycleExtraTime,
                firstCycleExtraTime=self.firstCycleExtraTime,
            )
        return None


def fishModel(filename, cycleReset, firstCycleExtra, days):
    population = []
    with open(filename) as file:
        for fishData in file.readline().split(","):
            population.append(Fish(cycleReset, firstCycleExtra, int(fishData)))
    for _ in range(days):
        newFish = []
        for individual in population:
            newborn = individual.update()
            if newborn:
                newFish.append(newborn)
        if newFish:
            population.extend(newFish)
    print([fish.timeToNext for fish in population])
    return len(population)


if __name__ == "__main__":
    result = fishModel("input.txt", cycleReset=6, firstCycleExtra=2, days=80)
    print(result)
