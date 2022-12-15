import json
from typing import Any, cast
import itertools
from functools import cmp_to_key
import pprint


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    datas: list[list[Any]] = []

    for line in lines:
        if line == "":
            continue

        datas.append(json.loads(line))

    datas.extend([[[2]], [[6]]])

    datas.sort(key=cmp_to_key(_compare_fn), reverse=True)

    i_for_2 = -1
    i_for_6 = -1

    for i, data in enumerate(datas):
        if data == [[2]]:
            i_for_2 = i
        elif data == [[6]]:
            i_for_6 = i

    print((i_for_2 + 1) * (i_for_6 + 1))


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
