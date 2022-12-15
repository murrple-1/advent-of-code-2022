from enum import IntEnum
import itertools
from typing import Callable, Generator


class EType(IntEnum):
    EMTPY = 0
    ROCK = 1
    SAND = 2


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    line_descriptors: list[list[tuple[int, int]]] = []

    all_x: set[int] = set()
    all_y: set[int] = set()

    for line in lines:
        line_descriptor: list[tuple[int, int]] = []
        for point_str in line.split(" -> "):
            x_str, y_str = point_str.split(",")

            x = int(x_str)
            y = int(y_str)
            line_descriptor.append((x, y))
            all_x.add(x)
            all_y.add(y)

        line_descriptors.append(line_descriptor)

    x_max = max(all_x) * 2
    y_max = max(all_y) + 2

    grid: list[list[EType]] = [
        [EType.EMTPY for _ in range(x_max + 1)] for _ in range(y_max + 1)
    ]

    for x in range(x_max + 1):
        grid[y_max][x] = EType.ROCK

    for line_descriptor in line_descriptors:
        for from_point, to_point in itertools.pairwise(line_descriptor):
            for x, y in _line_points(from_point, to_point):
                grid[y][x] = EType.ROCK

    current_sand_point: tuple[int, int] | None = None

    sands_dropped = 0
    while True:
        if current_sand_point is None:
            current_sand_point = _SAND_ORIGIN
            grid[current_sand_point[1]][current_sand_point[0]] = EType.SAND
        else:
            can_move, next_sand_point = _next_sand_point(
                current_sand_point, grid, x_max, y_max
            )

            if can_move is None:
                break

            if can_move:
                grid[next_sand_point[1]][next_sand_point[0]] = EType.SAND
                grid[current_sand_point[1]][current_sand_point[0]] = EType.EMTPY
                current_sand_point = next_sand_point
            else:
                sands_dropped += 1

                if current_sand_point == _SAND_ORIGIN:
                    break
                else:
                    current_sand_point = None

    print(sands_dropped)


def _line_points(
    from_point: tuple[int, int], to_point: tuple[int, int]
) -> Generator[tuple[int, int], None, None]:
    from_x, from_y = from_point
    to_x, to_y = to_point

    if from_x < to_x:
        for x in range(from_x, to_x + 1, 1):
            yield x, from_y
    elif from_x > to_x:
        for x in range(from_x, to_x - 1, -1):
            yield x, from_y
    elif from_y < to_y:
        for y in range(from_y, to_y + 1, 1):
            yield from_x, y
    elif from_y > to_y:
        for y in range(from_y, to_y - 1, -1):
            yield from_x, y


def _next_sand_point(
    current_sand_point: tuple[int, int], grid: list[list[EType]], x_max: int, y_max: int
) -> tuple[bool | None, tuple[int, int]]:
    for move_fn in _MOVE_FNS:
        potential_next_sand_point = move_fn(current_sand_point)

        if (
            0 <= potential_next_sand_point[0] <= x_max
            and 0 <= potential_next_sand_point[1] <= y_max
        ):
            grid_contains = grid[potential_next_sand_point[1]][
                potential_next_sand_point[0]
            ]
            if grid_contains in (EType.ROCK, EType.SAND):
                continue
            else:
                return True, potential_next_sand_point
        else:
            return None, potential_next_sand_point

    return False, (-1, -1)


_SAND_ORIGIN: tuple[int, int] = 500, 0

_MOVE_FNS: list[Callable[[tuple[int, int]], tuple[int, int]]] = [
    lambda p: (p[0], p[1] + 1),
    lambda p: (p[0] - 1, p[1] + 1),
    lambda p: (p[0] + 1, p[1] + 1),
]


if __name__ == "__main__":
    main()
