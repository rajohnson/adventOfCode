import re
import dataclasses
from typing import Optional
import collections


@dataclasses.dataclass
class Monkey:
    name: str
    value: Optional[int] = None
    operator: Optional[str] = None
    a: Optional[str] = None
    b: Optional[str] = None


DIGIT_RE = re.compile(r"(\w{4}): (\d+)")
COMPOUND_RE = re.compile(r"(\w{4}): (\w{4}) ([+\-*\/]) (\w{4})")


def find_value(monkey: Monkey) -> Optional[int]:
    if monkey.value is not None:
        return monkey.value
    return None


def build_monkeys(filename: str) -> dict[str, Monkey]:
    with open(filename, "r") as file_in:
        data = file_in.read()
    digit_monkeys = {
        match.group(1): Monkey(name=match.group(1), value=int(match.group(2)))
        for match in DIGIT_RE.finditer(data)
    }
    compound_monkeys = {
        match.group(1): Monkey(
            name=match.group(1),
            a=match.group(2),
            operator=match.group(3),
            b=match.group(4),
        )
        for match in COMPOUND_RE.finditer(data)
    }
    monkeys = {**digit_monkeys, **compound_monkeys}
    return monkeys


def part1(filename: str) -> int:
    monkeys = build_monkeys(filename)
    return monkeys
    # return monkeys["root"].value


def part2(filename: str):
    return None


if __name__ == "__main__":
    print(f"{part1('example.txt')=} 152")
    # print(f"{part1('input.txt')=}")
    # print(f"{part2('example.txt')=}")
    # print(f"{part2('input.txt')=}")
