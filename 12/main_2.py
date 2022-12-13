from collections import deque
from collections.abc import Generator


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    grid = [[c for c in line] for line in lines]

    y_len = len(grid)
    x_len = max(len(line) for line in grid)

    start_pos: tuple[int, int] = (-1, -1)
    end_pos: tuple[int, int] = (-1, -1)

    for j, line in enumerate(grid):
        for i, c in enumerate(line):
            pos = i, j
            if c == "S":
                start_pos = pos
            elif c == "E":
                end_pos = pos

    grid[start_pos[1]][start_pos[0]] = "z"

    starts: list[tuple[int, int]] = [
        (x, y) for y in range(y_len) for x in range(x_len) if grid[y][x] == "a"
    ]

    print(
        min(
            len(path) - 1
            for pos in starts
            if (path := _bfs(grid, x_len, y_len, pos, end_pos))
        )
    )


def _bfs(
    grid: list[list[str]],
    x_len: int,
    y_len: int,
    start_pos: tuple[int, int],
    end_pos: tuple[int, int],
) -> list[tuple[int, int]]:
    q: deque[list[tuple[int, int]]] = deque([[start_pos]])

    seen: set[tuple[int, int]] = set([start_pos])

    while len(q) > 0:
        path = q.popleft()
        current_pos = path[-1]

        if current_pos == end_pos:
            return path

        x, y = current_pos

        e = ord(grid[y][x])

        for neighbour_pos in _available_steps((x, y), x_len, y_len):
            if neighbour_pos not in seen:
                x2, y2 = neighbour_pos
                e2 = ord(grid[y2][x2]) if neighbour_pos != end_pos else ord("z")
                if e2 <= e + 1:
                    q.append(path + [(x2, y2)])
                    seen.add((x2, y2))

    return []


def _available_steps(
    pos: tuple[int, int], x_len: int, y_len: int
) -> Generator[tuple[int, int], None, None]:
    x, y = pos

    if x > 0:
        yield x - 1, y

    if y > 0:
        yield x, y - 1

    if x < x_len - 1:
        yield x + 1, y

    if y < y_len - 1:
        yield x, y + 1


if __name__ == "__main__":
    main()
