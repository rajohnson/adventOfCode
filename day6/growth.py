import collections
from typing import Counter


def fishModel(filename, cycleReset, firstCycleExtra, days):
    with open(filename) as file:
        population = collections.Counter()
        fishStates = map(int, file.readline().split(","))
        population.update(fishStates)
    for _ in range(days):
        updatedPopulation = collections.Counter()
        for day, number in population.items():
            if day <= 0:
                updatedPopulation[cycleReset] += number
                updatedPopulation[cycleReset + firstCycleExtra] += number
            else:
                updatedPopulation[day - 1] += number
        population = updatedPopulation
    return population.total()


if __name__ == "__main__":
    result = fishModel("input.txt", cycleReset=6, firstCycleExtra=2, days=256)
    print(result)
