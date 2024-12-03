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
    assert app.attempt("2024/day1/example.txt", 2) == 31


def test_get_counts() -> None:
    values = [1, 1, 2, 3, 3, 3]
    counts = app.get_counts(values)
    assert counts[1] == 2
    assert counts[2] == 1
    assert counts[3] == 3
    assert counts[4] == 0


def test_get_similarity_score() -> None:
    values = [1, 1, 2, 3, 3, 3]
    counts = app.get_counts(values)
    assert app.get_similarity_score(1, counts) == 2
    assert app.get_similarity_score(2, counts) == 2
    assert app.get_similarity_score(3, counts) == 9
    assert app.get_similarity_score(4, counts) == 0
