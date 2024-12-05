import day3


def test_get_input() -> None:
    memory = day3.get_input("2024/day3/example.txt")
    assert (
        memory
        == "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )


def test_get_instructions() -> None:
    memory = day3.get_input("2024/day3/example.txt")
    instructions = day3.get_instructions(memory)
    assert instructions == [(2, 4), (5, 5), (11, 8), (8, 5)]


def test_remove_disabled_instructions() -> None:
    start_memory = day3.get_input("2024/day3/example_part_2.txt")
    memory = day3.remove_disabled_instructions(start_memory)
    assert memory == "xmul(2,4)&mul[3,7]!^?mul(8,5))"


def test_example() -> None:
    assert day3.attempt("2024/day3/example.txt", 1) == 161
    assert day3.attempt("2024/day3/example_part_2.txt", 2) == 48
