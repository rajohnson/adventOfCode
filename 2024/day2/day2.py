def get_input(file_name: str) -> list[list[int]]:
    reports = []
    with open(file_name) as file:
        for line in file:
            reports.append([int(value) for value in line.split()])
    return reports


def report_is_safe(report: list[int], dampen: bool) -> bool:
    increasing = report[0] < report[1]
    i = 0
    j = 1
    while j < len(report):
        # change isn't consistent
        if (increasing and report[i] > report[j]) or (
            not increasing and report[i] < report[j]
        ):
            if not dampen:
                return False
            else:
                # drop the jth element and try again
                return report_is_safe(report[:j] + report[j + 1 :], False)

        # amount changed isn't within bounds
        if not (1 <= abs(report[i] - report[j]) <= 3):
            if not dampen:
                return False
            else:
                # drop the jth element and try again
                return report_is_safe(report[:j] + report[j + 1 :], False)

        # increment indices
        i += 1
        j += 1

    return True


def attempt(file_name: str, part: int) -> int:
    reports = get_input(file_name)
    if part == 1:
        return sum(report_is_safe(report, False) for report in reports)


if __name__ == "__main__":
    print(f'{attempt("2024/day2/input.txt", 1)=}')
