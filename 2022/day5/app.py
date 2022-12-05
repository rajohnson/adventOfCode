import collections
from typing import List
import math
import re


def create_stacks(stack_string: str) -> List[collections.deque]:
    lines = stack_string.split("\n")
    del lines[-1]  # strip out the numbering line
    num_stacks = math.ceil(len(lines[0]) / 4)
    stacks = [collections.deque() for _ in range(num_stacks)]
    for line in reversed(lines):
        for index, stack in enumerate(stacks):
            if (c := line[(index * 4) + 1]) != " ":
                stack.append(c)
    return stacks


def get_top_of_each_stack(stacks: List[collections.deque]) -> str:
    return "".join([stack.pop() for stack in stacks if len(stack)])


def execute_move(
    start: int, end: int, num: int, stacks: List[collections.deque]
) -> List[collections.deque]:
    for _ in range(num):
        stacks[end - 1].append(stacks[start - 1].pop())  # -1 since stacks are 1 indexed
    return stacks


def execute_moves(
    move_str: str, stacks: List[collections.deque]
) -> List[collections.deque]:
    for line in move_str.splitlines():
        print(line)
        match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
        num, start, end = match.groups()
        stacks = execute_move(int(start), int(end), int(num), stacks)
    return stacks


def part1(filename: str):
    with open(filename, "r") as file_in:
        data = file_in.read()
    stack_string, move_string = data.split("\n\n")
    starting_stacks = create_stacks(stack_string)
    end_stacks = execute_moves(move_string, starting_stacks)
    return get_top_of_each_stack(end_stacks)


if __name__ == "__main__":
    print(f"{part1('input.txt')=}")
