def get_input(file_name: str) -> list[list[int]]:
    reports = []
    with open(file_name) as file:
        for line in file:
            reports.append([int(value) for value in line.split()])
    return reports


def report_is_safe(report: list[int], dampen: bool) -> bool:
    unsafe_reports = 0
    increasing = report[0] < report[1]
    for i, j in zip(report, report[1:]):  # pair up adjacent values
        # change isn't consistent
        if (increasing and i > j) or (not increasing and i < j):
            unsafe_reports += 1
        # amount changed isn't within bounds
        if not (1 <= abs(i - j) <= 3):
            unsafe_reports += 1
    return unsafe_reports <= (1 if dampen else 0)


def attempt(file_name: str, part: int) -> int:
    reports = get_input(file_name)
    if part == 1:
        return sum(report_is_safe(report, False) for report in reports)


if __name__ == "__main__":
    print(f'{attempt("2024/day2/input.txt", 1)=}')
