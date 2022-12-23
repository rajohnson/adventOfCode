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


def get_unassigned_monkeys(monkeys: dict[str, Monkey]) -> list[Monkey]:
    unassigned_monkeys = [
        monkey for monkey in monkeys.values() if monkey.value is None
    ]
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
        return
    if monkeys[monkey.a].value is None or monkeys[monkey.b].value is None:
        return
    monkey.value = operation[monkey.operator](
        monkeys[monkey.a].value, monkeys[monkey.b].value
    )


def solve_backwards(
    monkey: Monkey, target: int, monkeys: dict[str, Monkey]
) -> None:
    # value is already set? - no need to continue
    if monkey.value is not None:
        return

    monkey.value = target

    # terminal monkey
    if monkey.a is None or monkey.b is None:
        return
    monkey_a = monkeys[monkey.a]
    monkey_b = monkeys[monkey.b]

    # not fully solved - solve and continue
    if monkey_a.value is None and monkey_b.value is None:
        solve_for_one_branch(monkey, monkeys)

    new_target = None
    # a is missing
    if monkey_a.value is None and monkey_b.value is not None:
        if monkey.operator == "+":
            new_target = monkey.value - monkey_b.value
        elif monkey.operator == "-":
            new_target = monkey.value + monkey_b.value
        elif monkey.operator == "*":
            new_target = monkey.value // monkey_b.value
        elif monkey.operator == "/":
            new_target = monkey.value * monkey_b.value
        else:
            raise NotImplementedError
        solve_backwards(monkey_a, new_target, monkeys)
    # b is missing
    elif monkey_b.value is None and monkey_a.value is not None:
        if monkey.operator == "+":
            new_target = monkey.value - monkey_a.value
        elif monkey.operator == "-":
            new_target = monkey_a.value - monkey.value
        elif monkey.operator == "*":
            new_target = monkey.value // monkey_a.value
        elif monkey.operator == "/":
            new_target = monkey_a.value // monkey.value
        else:
            raise NotImplementedError
        solve_backwards(monkey_b, new_target, monkeys)
    else:
        raise ValueError


def solve_for_one_branch(parent: Monkey, monkeys: dict[str, Monkey]) -> None:
    if parent.a is None or parent.b is None:
        raise ValueError("parent doesn't have child nodes to solve")
    child_a = monkeys[parent.a]
    child_b = monkeys[parent.b]
    while (
        child_a in (unassigned := get_unassigned_monkeys(monkeys))
        and child_b in unassigned
    ):
        for monkey in unassigned:
            find_value(monkey, monkeys)


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
    if monkeys["root"].value is None:
        raise ValueError("didn't solve completely")
    return monkeys["root"].value


def part2(filename: str) -> int:
    monkeys = build_monkeys(filename)

    root = monkeys["root"]
    if root.a is None or root.b is None:
        raise ValueError("root doesn't have (a) child node(s).")
    root_a = monkeys[root.a]
    root_b = monkeys[root.b]
    human = monkeys["humn"]

    # Don't solve anything that depends on the human
    human.value = None

    # solve as far as possible
    solve_for_one_branch(root, monkeys)

    # figure out value that is set
    target = root_a.value if root_a.value is not None else root_b.value
    if target is None:
        raise ValueError("both branches unsolved.")

    # solve from top downward
    if root_a.value is None:
        solve_backwards(root_a, target, monkeys)
    else:
        solve_backwards(root_b, target, monkeys)

    if human.value is None:
        raise ValueError("didn't calculate human value")
    return human.value


if __name__ == "__main__":
    print(f"{part1('example.txt')=} 152")
    print(f"{part1('input.txt')=}")
    print(f"{part2('example.txt')=} 301")
    print(f"{part2('input.txt')=}")
