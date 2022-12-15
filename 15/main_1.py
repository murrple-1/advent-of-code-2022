import re
from dataclasses import dataclass
from enum import IntEnum
from collections import defaultdict
from typing import Generator


@dataclass
class Sensor:
    pos: tuple[int, int]
    closest_beacon_pos: tuple[int, int]


class EType(IntEnum):
    UNKNOWN = 0
    SENSOR = 1
    BEACON = 2
    NO_BEACON = 3


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    sensors: list[Sensor] = []

    all_x: set[int] = set()
    all_y: set[int] = set()

    for line in lines:
        match = re.match(
            r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
            line,
        )
        assert match

        sensor = Sensor(
            (int(match.group(1)), int(match.group(2))),
            (int(match.group(3)), int(match.group(4))),
        )

        sensors.append(sensor)

        all_x.add(sensor.pos[0])
        all_x.add(sensor.closest_beacon_pos[0])
        all_y.add(sensor.pos[1])
        all_y.add(sensor.closest_beacon_pos[1])

    x_min = min(all_x)
    x_max = max(all_x)
    y_min = min(all_y)
    y_max = max(all_y)

    grid: dict[tuple[int, int], EType] = defaultdict(lambda: EType.UNKNOWN)

    for sensor in sensors:
        grid[sensor.pos] = EType.SENSOR
        grid[sensor.closest_beacon_pos] = EType.BEACON

    for sensor in sensors:
        for pos in _manhattan_grid(sensor.pos, sensor.closest_beacon_pos):
            grid[pos] = (
                EType.NO_BEACON if (etype := grid[pos]) == EType.UNKNOWN else etype
            )

    count_no_beacon = 0
    for x in range(x_min, x_max + 1, 1):
        if grid[(x, _RELEVANT_ROW)] == EType.NO_BEACON:
            count_no_beacon += 1

    print(count_no_beacon)


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


_RELEVANT_ROW = 2000000


if __name__ == "__main__":
    main()
