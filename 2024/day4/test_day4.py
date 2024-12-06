import day4
import pytest


def test_get_input() -> None:
    puzzle = day4.get_input("2024/day4/example.txt")
    assert puzzle == [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]


@pytest.mark.parametrize(
    "word, line, expected",
    [
        ("XMAS", "XMAQSAMXAMM", 0),
        ("XMAS", "XMASAMXAMM", 1),
        ("XMAS", "XMASAMXAMMXMAS", 2),
        ("XMAS", "XMASAMXAMMXMASXMAS", 3),
    ],
)
def test_count_word(word: str, line: str, expected: int) -> None:
    assert day4.count_word(word, line) == expected


def test_count_words_horizontal() -> None:
    lines = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]
    assert day4.count_words_horizontal("XMAS", lines) == 5


def test_count_words_vertical() -> None:
    lines = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]
    assert day4.count_words_vertical("XMAS", lines) == 3


def test_count_words_diagonal() -> None:
    lines = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]
    assert day4.count_words_diagonal("XMAS", lines) == 10


def test_count_words_h() -> None:
    lines = ["..X...", ".SAMX.", ".A..A.", "XMAS.S", ".X...."]
    assert day4.count_words_horizontal("XMAS", lines) == 2


def test_count_words_v() -> None:
    lines = ["..X...", ".SAMX.", ".A..A.", "XMAS.S", ".X...."]
    assert day4.count_words_vertical("XMAS", lines) == 1


def test_count_words_d() -> None:
    lines = ["..X...", ".SAMX.", ".A..A.", "XMAS.S", ".X...."]
    assert day4.count_words_diagonal("XMAS", lines) == 1


def test_count_words_all() -> None:
    lines = ["..X...", ".SAMX.", ".A..A.", "XMAS.S", ".X...."]
    assert day4.count_words_all("XMAS", lines) == 4


def test_example() -> None:
    assert day4.attempt("2024/day4/example.txt", 1) == 18
