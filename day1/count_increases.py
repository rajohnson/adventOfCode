import math


def count_increases(filename):
    count = 0
    with open(filename, mode="r") as file:
        last = math.inf  # prevents the first reading from increasing.
        for line in file:
            if int(line) > last:
                count += 1
            last = int(line)
    return count


if __name__ == "__main__":
    print(count_increases("./input.txt"))
