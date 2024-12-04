import day2
import pytest


@pytest.mark.parametrize(
    "report, result",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_report_is_safe(report, result) -> None:
    assert day2.report_is_safe(report) == result


def test_get_input() -> None:
    reports = day2.get_input("2024/day2/example.txt")
    assert reports[0] == [7, 6, 4, 2, 1]


def test_example() -> None:
    assert day2.attempt("2024/day2/example.txt", 1) == 2
