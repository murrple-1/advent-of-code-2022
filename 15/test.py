from typing import Generator


def main():
    x_max = 20
    y_max = 20

    grid: list[list[int]] = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]

    s = 5, 6
    b = 2, 8

    grid[s[1]][s[0]] = 1
    grid[b[1]][b[0]] = 2

    for i, (x, y) in enumerate(_manhattan_grid(s, b)):
        if 0 <= x <= x_max and 0 <= y <= y_max:
            grid[y][x] = 3 if grid[y][x] == 0 else grid[y][x]
            _print_grid(grid)
            print()
            print()


def _manhattan_grid(
    from_pos: tuple[int, int], to_pos: tuple[int, int]
) -> Generator[tuple[int, int], None, None]:
    from_x, from_y = from_pos
    to_x, to_y = to_pos

    longest_length = abs(from_x - to_x) + abs(from_y - to_y) + 1

    for y in range(longest_length):
        for step in range(longest_length + 1):
            for x in range(step):
                yield from_x + x, from_y + longest_length - step
                yield from_x + x, from_y - longest_length + step
                yield from_x - x, from_y + longest_length - step
                yield from_x - x, from_y - longest_length + step


def _print_grid(grid: list[list[int]]):
    import sys

    for line in grid:
        for b in line:
            if b == 0:
                sys.stdout.write(".")
            elif b == 1:
                sys.stdout.write("S")
            elif b == 2:
                sys.stdout.write("B")
            elif b == 3:
                sys.stdout.write("#")
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
