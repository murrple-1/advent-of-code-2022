import json
from typing import Any, cast
import itertools


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    pairs: list[tuple[list[Any], list[Any]]] = []

    p1: list[Any] | None = None
    p2: list[Any] | None = None

    for line in lines:
        if line == "":
            continue

        if p1 is None:
            p1 = json.loads(line)
        elif p2 is None:
            p2 = json.loads(line)

        if p1 is not None and p2 is not None:
            pairs.append((p1, p2))

            p1 = None
            p2 = None

    if p1 is not None and p2 is not None:
        pairs.append((p1, p2))

    sum_of_good_pairs = 0

    for i, (left, right) in enumerate(pairs):
        i += 1

        is_in_order = _compare_fn(left, right)
        if is_in_order > 0:
            sum_of_good_pairs += i

    print(sum_of_good_pairs)


def _compare_fn(left: list[Any] | int, right: list[Any] | int) -> int:
    if type(left) is int:
        if type(right) is int:
            return right - left
        else:
            return _compare_fn([left], right)
    else:
        if type(right) is int:
            return _compare_fn(left, [right])
        else:
            for left_v, right_v in itertools.zip_longest(
                cast(list[Any], left), cast(list[Any], right), fillvalue=None
            ):
                if left_v is None:
                    return 1

                if right_v is None:
                    return -1

                is_in_order = _compare_fn(left_v, right_v)
                if is_in_order != 0:
                    return is_in_order

            return 0


if __name__ == "__main__":
    main()
