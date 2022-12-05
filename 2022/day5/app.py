import collections
from typing import List, Deque
import math


def create_stacks(stack_string: str) -> List[Deque[str]]:
    lines = stack_string.split("\n")
    del lines[-1]  # strip out the numbering line
    num_stacks = math.ceil(len(lines[0]) / 4)
    stacks: List[Deque[str]] = [collections.deque() for _ in range(num_stacks)]
    for line in reversed(lines):
        for index, stack in enumerate(stacks):
            if (c := line[(index * 4) + 1]) != " ":
                stack.append(c)
    return stacks


def get_top_of_each_stack(stacks: List[Deque[str]]) -> str:
    return "".join([stack.pop() for stack in stacks if len(stack)])


def execute_move(
    start: int, end: int, num: int, stacks: List[Deque[str]], isPart2: bool
) -> List[Deque[str]]:
    start, end = start - 1, end - 1  # -1 since stacks are 1 indexed instead of 0
    if isPart2:
        values = reversed([stacks[start].pop() for _ in range(num)])
        stacks[end].extend(values)
    else:
        for _ in range(num):
            stacks[end].append(stacks[start].pop())
    return stacks


def execute_moves(
    move_str: str, stacks: List[Deque[str]], isPart2=False
) -> List[Deque[str]]:
    for line in move_str.splitlines():
        _, num, _, start, _, end = line.split()
        stacks = execute_move(int(start), int(end), int(num), stacks, isPart2)
    return stacks


def part1(filename: str) -> str:
    with open(filename, "r") as file_in:
        data = file_in.read()
    stack_string, move_string = data.split("\n\n")
    starting_stacks = create_stacks(stack_string)
    end_stacks = execute_moves(move_string, starting_stacks)
    return get_top_of_each_stack(end_stacks)


def part2(filename: str) -> str:
    with open(filename, "r") as file_in:
        data = file_in.read()
    stack_string, move_string = data.split("\n\n")
    starting_stacks = create_stacks(stack_string)
    end_stacks = execute_moves(move_string, starting_stacks, isPart2=True)
    return get_top_of_each_stack(end_stacks)


if __name__ == "__main__":
    print(f"{part1('input.txt')=}")
    print(f"{part2('input.txt')=}")
