import app


def test_get_distances() -> None:
    a = [9, 6, 3]
    b = [3, 5, 4]
    assert app.get_distances(a, b) == [0, 2, 4]


def test_get_input() -> None:
    assert app.get_input("2024/day1/example.txt") == (
        [3, 4, 2, 1, 3, 3],
        [4, 3, 5, 3, 9, 3],
    )


def test_example() -> None:
    assert app.attempt("2024/day1/example.txt", 1) == 11
