def get_signal_strength(history: list[int], cycle_of_interest: int) -> int:
    return history[cycle_of_interest - 1] * cycle_of_interest


def build_system_state_history(filename: str) -> list[int]:
    with open(filename, "r") as file_in:
        data = file_in.readlines()
    accumulator = 1
    history = []
    for line in data:
        if line.startswith("noop"):
            history.append(accumulator)
        elif line.startswith("addx"):
            history.append(accumulator)
            history.append(accumulator)
            _, value = line.split()
            accumulator += int(value)
        else:
            raise NotImplementedError
    return history


def part1(filename: str):
    system_status = build_system_state_history(filename)
    cycles_of_interest = [20 + 40 * i for i in range(6)]
    signal_strengths = [
        get_signal_strength(system_status, cycle)
        for cycle in cycles_of_interest
    ]

    return sum(signal_strengths)


def render_screen(screen: list[str]) -> None:
    screen_str = "".join(screen)
    print("\n\n")
    for i in range(6):
        print(f"{screen_str[40*i:40*(i+1)]}")


def part2(filename: str):
    system_status = build_system_state_history(filename)
    screen = ["." for _ in range(240)]
    for cycle, x in enumerate(system_status):
        position = cycle % 40
        sprite = set([x - 1, x, x + 1])
        if position in sprite:
            screen[cycle] = "#"
    render_screen(screen)
    return None


if __name__ == "__main__":
    print(f"{part1('input.txt')=}")
    print(f"{part2('input.txt')=}")
