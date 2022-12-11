import dataclasses
import re
import functools


@dataclasses.dataclass
class Monkey:
    id: int
    items: list[int]
    operation: str
    divisibility_num: int
    dest_true: int
    dest_false: int
    inspections: int = 0

    @classmethod
    def from_str(cls, monkey_str: str):
        monkey_match = re.match(
            (
                r"Monkey (\d)+:\n  Starting items: (.*)\n  Operation: (.*)\n"
                r"  Test: divisible by (\d+)\n    If true: throw to monkey"
                r" (\d+)\n    If false: throw to monkey (\d+)"
            ),
            monkey_str,
        )
        id, items, operation, divisibility_num, dest_true, dest_false = [
            monkey_match.group(i + 1) for i in range(6)
        ]
        return cls(
            id=int(id),
            items=[int(item) for item in items.split(",")],
            operation=operation,
            divisibility_num=int(divisibility_num),
            dest_true=int(dest_true),
            dest_false=int(dest_false),
        )


def get_monkeys(filename: str) -> list[Monkey]:
    with open(filename, "r") as file_in:
        data = file_in.read()
    data = data.replace("old", "item").replace("new = ", "")
    monkeys = [
        Monkey.from_str(monkey_str) for monkey_str in data.split("\n\n")
    ]
    return monkeys


def run_round(monkeys: list[Monkey], worry_change: callable) -> None:
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspections += 1
            item = eval(monkey.operation, {}, {"item": item})
            item = worry_change(item)
            if item % monkey.divisibility_num == 0:
                monkeys[monkey.dest_true].items.append(item)
            else:
                monkeys[monkey.dest_false].items.append(item)
        monkey.items = []


def part1(filename: str):
    monkeys = get_monkeys(filename)
    for round in range(20):
        run_round(monkeys, lambda x: x // 3)
    a, b = sorted([monkey.inspections for monkey in monkeys])[-2:]
    return a * b


def part2(filename: str):
    monkeys = get_monkeys(filename)
    divisibilty_product = functools.reduce(
        lambda a, b: a * b, (monkey.divisibility_num for monkey in monkeys)
    )
    for round in range(10_000):
        run_round(monkeys, lambda x: x % divisibilty_product)
    a, b = sorted([monkey.inspections for monkey in monkeys])[-2:]
    return a * b


if __name__ == "__main__":
    print(f"{part1('input.txt')=}")
    print(f"{part2('input.txt')=}")
