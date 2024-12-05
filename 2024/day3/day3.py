import re


def get_input(file_name: str) -> str:
    with open(file_name) as file:
        return file.read()


def get_instructions(memory: str) -> list[tuple[int, int]]:
    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = regex.finditer(memory)
    result = []
    for match in matches:
        result.append((int(match.group(1)), int(match.group(2))))
    return result


def get_instruction_value(instruction: tuple[int, int]) -> int:
    a, b = instruction
    return a * b


def remove_disabled_instructions(memory: str) -> str:
    regex = re.compile(r"don't\(\).*?((do\(\))|\Z)")
    return regex.sub("", memory)


def attempt(file_name: str, part: int) -> int:
    memory = get_input(file_name)
    if part == 1:
        return sum(
            get_instruction_value(instruction)
            for instruction in get_instructions(memory)
        )
    elif part == 2:
        return sum(
            get_instruction_value(instruction)
            for instruction in get_instructions(remove_disabled_instructions(memory))
        )


if __name__ == "__main__":
    print()
    print(f'{attempt("2024/day3/input.txt", 1)=}')
    print(f'{attempt("2024/day3/input.txt", 2)=}')
