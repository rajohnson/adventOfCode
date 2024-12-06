import itertools


def get_input(file_name: str) -> list[str]:
    with open(file_name) as file:
        return file.read().splitlines()


def count_word(word: str, line: str) -> int:  # only will find in standard order
    return line.count(word)


def count_words_horizontal(word: str, lines: str) -> int:
    forward_count = sum(count_word(word, line) for line in lines)
    backward_count = sum(count_word(word, line[::-1]) for line in lines)
    return forward_count + backward_count


def count_words_vertical(word: str, lines: str) -> int:
    transposed_lines = ["".join(line) for line in zip(*lines)]
    return count_words_horizontal(word, transposed_lines)


def count_words_diagonal(word: str, lines: str) -> int:
    right_shifted_lines = [" " * i + line for i, line in enumerate(lines)]
    left_shifted_lines = [" " * i + line for i, line in enumerate(lines[::-1])]
    right_diagonals = [
        "".join(line)
        for line in itertools.zip_longest(*right_shifted_lines, fillvalue=" ")
    ]
    left_diagonals = [
        "".join(line)
        for line in itertools.zip_longest(*left_shifted_lines, fillvalue=" ")
    ]
    return count_words_horizontal(word, right_diagonals) + count_words_horizontal(
        word, left_diagonals
    )


def count_words_all(word: str, lines: str) -> int:
    return (
        count_words_horizontal(word, lines)
        + count_words_vertical(word, lines)
        + count_words_diagonal(word, lines)
    )


def attempt(file_name: str, part: int) -> int:
    word = "XMAS"
    lines = get_input(file_name)
    if part == 1:
        return count_words_all(word, lines)


if __name__ == "__main__":
    print()
    print(f'{attempt("2024/day4/input.txt", 1)=}')
    print(f'{attempt("2024/day4/input.txt", 2)=}')
