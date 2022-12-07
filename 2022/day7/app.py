import collections
from typing import Union, List, TypeVar
import dataclasses


File = collections.namedtuple("File", "name size")

Directory = TypeVar("Directory")


@dataclasses.dataclass
class Directory:
    name: str
    content: List[Union[Directory, File]]
    parent: Directory
    size: Union[None, int]

    def __repr__(self) -> str:
        return (
            f"Directory({self.name}, parent={self.parent.name}, size={self.size}, "
            f"content={self.content})"
        )


max_size = 100_000
capacity = 70_000_000
required_space = 30_000_000


def find_root(current_dir: Union[Directory, None]) -> Union[Directory, None]:
    if not current_dir:
        return None

    while current_dir.parent is not None:
        current_dir = current_dir.parent
    return current_dir


def get_list_of_directories(directory: Directory) -> List[Directory]:
    directory_list = [directory]
    for item in directory.content:
        if isinstance(item, Directory):
            directory_list += get_list_of_directories(item)
    return directory_list


def assign_directory_sizes(directory: Directory) -> None:
    total = 0
    for item in directory.content:
        if item.size is None:
            assign_directory_sizes(item)
        total += item.size
    directory.size = total


# builds the tree of the file system
def process_command(line: str, current_dir: Union[Directory, None]) -> Directory:
    lines = line.splitlines()
    command = lines.pop(0)
    if command.startswith("cd"):
        _, target_name = line.split()
        if current_dir is None:
            if target_name == "/":
                return Directory("/", [], None, None)
            else:
                raise ValueError("Root directory has not been created yet.")

        if target_name == "..":
            return current_dir.parent

        for content in current_dir.content:
            if not isinstance(content, Directory):
                continue
            if content.name == target_name:
                return content
        raise ValueError("Couldn't find the specified directory.")

    elif command == "ls":
        for line in lines:
            size, name = line.split()
            if size.isdigit():
                current_dir.content.append(File(name, int(size)))
            else:
                current_dir.content.append(Directory(name, [], current_dir, None))
        return current_dir

    else:
        raise NotImplementedError("Unrecognized command.")


def generate_directory_tree(filename: str) -> Directory:
    with open(filename, "r") as file_in:
        command_groups = [
            cmd_stripped
            for cmd in file_in.read().split("$")
            if (cmd_stripped := cmd.strip())
        ]

    # build a tree from the commands
    directory: Union[Directory, None] = None
    for command_group in command_groups:
        directory = process_command(command_group, directory)

    root = find_root(directory)

    assign_directory_sizes(root)

    return root


def part1(filename: str):
    root_directory = generate_directory_tree(filename)
    return sum(
        directory.size
        for directory in get_list_of_directories(root_directory)
        if directory.size <= max_size
    )


def part2(filename: str):
    root_directory = generate_directory_tree(filename)
    directories = get_list_of_directories(root_directory)
    total_space = max(directory.size for directory in directories)
    free_space = capacity - total_space
    space_needed = required_space - free_space
    return min(
        directory.size for directory in directories if directory.size >= space_needed
    )


if __name__ == "__main__":
    print(f"{part1('input.txt')=}")
    print(f"{part2('input.txt')=}")
