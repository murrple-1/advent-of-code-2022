from typing import Callable, Generator
import math


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    tree_grid: list[list[int]] = []
    scenic_score_grid: list[list[int]] = []

    for line in lines:
        tree_grid.append([int(c) for c in line])
        scenic_score_grid.append([0 for _ in line])

    x_len = len(tree_grid)
    y_len = max(len(line) for line in tree_grid)

    for x in range(x_len):
        for y in range(y_len):
            max_height = tree_grid[y][x]
            scenic_score_grid[y][x] = math.prod(
                _direction_scenic_score(max_height, tree_grid, rg(x, y, x_len, y_len))
                for rg in _RAY_GENERATORS
            )

    print(max(max(line) for line in scenic_score_grid))


def _down(
    start_x: int, start_y: int, _x_len: int, y_len: int
) -> Generator[tuple[int, int], None, None]:
    for y in range(start_y + 1, y_len):
        yield start_x, y


def _up(
    start_x: int, start_y: int, _x_len: int, _y_len: int
) -> Generator[tuple[int, int], None, None]:
    for y in range(start_y - 1, -1, -1):
        yield start_x, y


def _right(
    start_x: int, start_y: int, x_len: int, _y_len: int
) -> Generator[tuple[int, int], None, None]:
    for x in range(start_x + 1, x_len):
        yield x, start_y


def _left(
    start_x: int, start_y: int, _x_len: int, _y_len: int
) -> Generator[tuple[int, int], None, None]:
    for x in range(start_x - 1, -1, -1):
        yield x, start_y


_RAY_GENERATORS: list[
    Callable[[int, int, int, int], Generator[tuple[int, int], None, None]]
] = [
    _down,
    _up,
    _right,
    _left,
]


def _direction_scenic_score(
    max_height: int,
    tree_grid: list[list[int]],
    generator: Generator[tuple[int, int], None, None],
) -> int:
    score = 0
    for x, y in generator:
        if tree_grid[y][x] >= max_height:
            return score + 1
        else:
            score += 1

    return score


if __name__ == "__main__":
    main()
