# find the first and last digit in a string and make them into a two digit number
def calibrate(line: str) -> int:
    while not line[0].isdigit():
        line = line[1:]

    while not line[-1].isdigit():
        line = line[:-1]

    first = line[0]
    last = line[-1]

    return int(first) * 10 + int(last)


# get sum of the calibration value for each line in file_name
def attempt(file_name: str) -> int:
    total = 0
    with open(file_name, "r") as data_in:
        for line in data_in:
            total += calibrate(line)

    return total


if __name__ == "__main__":
    print(f'{attempt("input.txt")=}')
