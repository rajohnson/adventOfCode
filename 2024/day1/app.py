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


def attempt(file_name: str, part: int) -> int:
    a, b = get_input(file_name)
    distances = get_distances(a, b)
    if part == 1:
        return sum(distances)


if __name__ == "__main__":
    print(f'{attempt("2024/day1/input.txt", 1)=}')
