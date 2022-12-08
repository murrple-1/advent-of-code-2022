from typing import Generator, Callable


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    tree_grid: list[list[int]] = []
    visible_grid: list[list[bool]] = []

    for line in lines:
        tree_grid.append([int(c) for c in line])
        visible_grid.append([False for _ in line])

    x_len = len(tree_grid)
    y_len = max(len(line) for line in tree_grid)

    for ray_generator in _RAY_GENERATORS:
        blocking_height = 0
        for start, x, y in ray_generator(x_len, y_len):
            if start:
                visible_grid[y][x] = True
                blocking_height = tree_grid[y][x]
            else:
                if (height := tree_grid[y][x]) > blocking_height:
                    visible_grid[y][x] = True
                    blocking_height = height
                else:
                    visible_grid[y][x] = visible_grid[y][x] or False

    print(sum(sum(1 if c else 0 for c in line) for line in visible_grid))


def _top_down(x_len: int, y_len: int) -> Generator[tuple[bool, int, int], None, None]:
    for x in range(x_len):
        start = True
        for y in range(0, y_len):
            yield start, x, y
            start = False


def _bottom_up(x_len: int, y_len: int) -> Generator[tuple[bool, int, int], None, None]:
    for x in range(x_len):
        start = True
        for y in range(y_len - 1, -1, -1):
            yield start, x, y
            start = False


def _left_right(x_len: int, y_len: int) -> Generator[tuple[bool, int, int], None, None]:
    for y in range(y_len):
        start = True
        for x in range(0, x_len):
            yield start, x, y
            start = False


def _right_left(x_len: int, y_len: int) -> Generator[tuple[bool, int, int], None, None]:
    for y in range(y_len):
        start = True
        for x in range(x_len - 1, -1, -1):
            yield start, x, y
            start = False


_RAY_GENERATORS: list[
    Callable[[int, int], Generator[tuple[bool, int, int], None, None]]
] = [
    _top_down,
    _bottom_up,
    _left_right,
    _right_left,
]


if __name__ == "__main__":
    main()
