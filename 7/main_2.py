from dataclasses import dataclass
import re
from typing import Generator, Union


@dataclass
class Directory:
    name: str
    files: dict[str, "File"]
    directories: dict[str, "Directory"]
    parent: Union["Directory", None]

    @property
    def size(self):
        return sum(f.size for f in self.files.values()) + sum(
            d.size for d in self.directories.values()
        )


@dataclass
class File:
    name: str
    size: int


@dataclass
class Command:
    cmd: list[str]
    output: list[str]


TOTAL_MEMORY = 70000000
REQUIRED_MEMORY_FOR_UPDATE = 30000000


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    root_directory = Directory("/", {}, {}, None)

    cwd = root_directory

    current_cmd: Command | None = None

    for line in lines:
        if line.startswith("$"):
            if current_cmd is not None:
                cwd = _handle_command(current_cmd, cwd, root_directory)

            current_cmd = Command(line.split(" "), [])
        else:
            if current_cmd is not None:
                current_cmd.output.append(line)

    if current_cmd is not None:
        cwd = _handle_command(current_cmd, cwd, root_directory)

    current_free_space = TOTAL_MEMORY - root_directory.size

    print(
        min(
            d.size
            for d in _all_directories(root_directory)
            if (current_free_space + d.size) >= REQUIRED_MEMORY_FOR_UPDATE
        )
    )


def _handle_command(
    cmd: Command, cwd: Directory, root_directory: Directory
) -> Directory:
    if cmd.cmd[1] == "ls":
        for line in cmd.output:
            line_split = line.split(" ")
            if line_split[0] == "dir":
                subdir_name = line_split[1]
                if subdir_name not in cwd.directories:
                    cwd.directories[subdir_name] = Directory(subdir_name, {}, {}, cwd)
            else:
                file_name = line_split[1]
                cwd.files[file_name] = File(file_name, int(line_split[0]))

        return cwd
    elif cmd.cmd[1] == "cd":
        to_dir = cmd.cmd[2]

        if to_dir == "/":
            return root_directory
        elif to_dir == "..":
            assert cwd.parent
            return cwd.parent
        else:
            return cwd.directories[to_dir]
    else:
        raise AssertionError


def _all_directories(dir_: Directory) -> Generator[Directory, None, None]:
    yield dir_

    for subdir in dir_.directories.values():
        for d in _all_directories(subdir):
            yield d


if __name__ == "__main__":
    main()
