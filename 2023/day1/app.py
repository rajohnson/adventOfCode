# find the first and last digit in a string and make them into a two digit number
def calibrate(line: str) -> int:
    while not line[0].isdigit():
        line = line[1:]

    while not line[-1].isdigit():
        line = line[:-1]

    first = line[0]
    last = line[-1]

    return int(first) * 10 + int(last)


# find the first and last digit in a string and make them into a two digit number digits can be actual digits or the english word for the digit
def calibrate_text(line: str) -> int:
    raise NotImplementedError


# get sum of the calibration value for each line in file_name
def attempt(file_name: str, part: int) -> int:
    total = 0
    with open(file_name, "r") as data_in:
        for line in data_in:
            if part == 1:
                total += calibrate(line)
            elif part == 2:
                total += calibrate_text(line)
            else:
                raise ValueError(f"part must be 1 or 2, not {part}")

    return total


if __name__ == "__main__":
    print(f'{attempt("input.txt", 1)=}')
    print(f'{attempt("input.txt", 2)=}')
