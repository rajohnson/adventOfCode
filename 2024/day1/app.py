import collections


def get_distances(a: list[int], b: list[int]) -> list[int]:
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    distance = [abs(a_val - b_val) for a_val, b_val in zip(a_sorted, b_sorted)]
    return distance


def get_input(file_name: str) -> tuple[list[int], list[int]]:
    a = []
    b = []
    with open(file_name) as file:
        for line in file:
            a_val, b_val = line.split()
            a.append(int(a_val))
            b.append(int(b_val))
    return a, b


def get_counts(a: list[int]) -> dict[int, int]:
    return collections.Counter(a)


def get_similarity_score(value: int, counts: dict[int, int]) -> int:
    return value * counts[value]


def attempt(file_name: str, part: int) -> int:
    a, b = get_input(file_name)
    if part == 1:
        distances = get_distances(a, b)
        return sum(distances)
    elif part == 2:
        counts = get_counts(b)
        return sum(get_similarity_score(value, counts) for value in a)


if __name__ == "__main__":
    print(f'{attempt("2024/day1/input.txt", 1)=}')
    print(f'{attempt("2024/day1/input.txt", 2)=}')
