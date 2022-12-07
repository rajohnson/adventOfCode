import collections
from typing import Union, List

Directory = collections.namedtuple("Directory", "name content parent")
File = collections.namedtuple("File", "name size")
DirectorySize = collections.namedtuple("DirectorySize", "name size")

max_size = 100_000
capacity = 70_000_000
required_space = 30_000_000


def find_root(current_dir: Union[Directory, None]) -> Union[Directory, None]:
    if not current_dir:
        return None

    while current_dir.parent is not None:
        current_dir = current_dir.parent

    return current_dir


def get_list_of_directory_sizes(directory: Directory) -> List[int]:
    size_list = [DirectorySize(directory.name, find_directory_size(directory))]
    for item in directory.content:
        if isinstance(item, Directory):
            size_list += get_list_of_directory_sizes(item)
    return size_list


def find_directory_size(directory: Directory) -> int:
    total = 0
    for item in directory.content:
        if isinstance(item, File):
            total += item.size
        else:
            total += find_directory_size(item)
    return total


# builds the tree of the file system
def process_command(line: str, current_dir: Union[Directory, None]) -> Directory:
    lines = line.splitlines()
    command = lines.pop(0)
    if command.startswith("cd"):
        _, target_name = line.split()
        if current_dir is None:
            if target_name == "/":
                return Directory("/", [], None)
            else:
                raise ValueError

        if target_name == "..":
            return current_dir.parent

        for content in current_dir.content:
            if not isinstance(content, Directory):
                continue
            if content.name == target_name:
                return content
        raise ValueError

    elif command == "ls":
        for line in lines:
            size, name = line.split()
            if size.isdigit():
                current_dir.content.append(File(name, int(size)))
            else:
                current_dir.content.append(Directory(name, [], current_dir))
        return current_dir

    else:
        raise NotImplementedError


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

    return find_root(directory)


def part1(filename: str):
    root_directory = generate_directory_tree(filename)
    return sum(
        [
            directory.size
            for directory in get_list_of_directory_sizes(root_directory)
            if directory.size <= max_size
        ]
    )


def part2(filename: str):
    root_directory = generate_directory_tree(filename)
    directory_sizes = get_list_of_directory_sizes(root_directory)
    total_space = max(directory_sizes, key=lambda x: x.size).size
    free_space = capacity - total_space
    space_needed = required_space - free_space
    return min(
        [directory for directory in directory_sizes if directory.size >= space_needed],
        key=lambda x: x.size,
    ).size


if __name__ == "__main__":
    print(f"{part1('input.txt')=}")
    print(f"{part2('input.txt')=}")
