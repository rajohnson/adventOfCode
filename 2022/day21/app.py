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


def get_unassigned_monkeys(monkeys: dict[int, Monkey]) -> list[Monkey]:
    unassigned_monkeys = [monkey for monkey in monkeys.values() if monkey.value is None]
    return unassigned_monkeys


def find_value(monkey: Monkey, monkeys: dict[str, Monkey]) -> None:
    operation = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a // b,
    }
    if monkey.value is not None:
        return
    if (
        monkey.a is None
        or monkey.b is None
        or monkey.operator is None
        or monkey.operator not in operation
    ):
        raise ValueError
    if monkeys[monkey.a].value is None or monkeys[monkey.b].value is None:
        return
    monkey.value = operation[monkey.operator](
        monkeys[monkey.a].value, monkeys[monkey.b].value
    )


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
    while unassigned := get_unassigned_monkeys(monkeys):
        for monkey in unassigned:
            find_value(monkey, monkeys)
    return monkeys


def part1(filename: str) -> int:
    monkeys = build_monkeys(filename)
    return monkeys["root"].value


def part2(filename: str):
    return None


if __name__ == "__main__":
    print(f"{part1('example.txt')=} 152")
    print(f"{part1('input.txt')=} 43699799094202")
    # print(f"{part2('example.txt')=}")
    # print(f"{part2('input.txt')=}")
