import copy
import re
import dataclasses
from typing import Optional


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
        "/": lambda a, b: a / b,
    }
    if monkey.value is not None:
        return
    if (
        monkey.a is None
        or monkey.b is None
        or monkey.operator is None
        or monkey.operator not in operation
    ):
        return
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
    return monkeys


def part1(filename: str) -> int:
    monkeys = build_monkeys(filename)
    while unassigned := get_unassigned_monkeys(monkeys):
        for monkey in unassigned:
            find_value(monkey, monkeys)
    return monkeys["root"].value


def part2(filename: str) -> int:
    original_monkeys = build_monkeys(filename)
    original_monkeys["humn"].value = None
    root_a = original_monkeys[original_monkeys["root"].a]
    root_b = original_monkeys[original_monkeys["root"].b]
    # solve as far as possible
    while (
        root_a in (unassigned := get_unassigned_monkeys(original_monkeys))
        and root_b in unassigned
    ):
        for monkey in unassigned:
            find_value(monkey, original_monkeys)
    # figure out which is target
    target = (
        original_monkeys[original_monkeys["root"].a].value
        if original_monkeys[original_monkeys["root"].a].value is not None
        else original_monkeys[original_monkeys["root"].b].value
    )
    test_value = 0
    while True:
        monkeys = copy.deepcopy(original_monkeys)
        root_a = monkeys[monkeys["root"].a]
        root_b = monkeys[monkeys["root"].b]
        monkeys["humn"].value = test_value  # set the new test_value

        # solve
        while unassigned := get_unassigned_monkeys(monkeys):
            for monkey in unassigned:
                find_value(monkey, monkeys)

        # test to see if the values are equal
        if root_a.value == root_b.value:
            break
        else:
            test_value += 1
    return test_value


if __name__ == "__main__":
    print(f"{part1('example.txt')=} 152")
    print(f"{part1('input.txt')=} 43699799094202")
    print(f"{part2('example.txt')=} 301")
    print(
        f"{part2('input.txt')=} 3375719472770"
    )  # found this with binary search in debugger...brute force wasn't working
