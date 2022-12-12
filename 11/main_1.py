from collections.abc import Callable
from dataclasses import dataclass, field
import re
import math
import functools


def _fake_operation(i: int) -> int:
    raise NotImplementedError


def _fake_test(i: int) -> bool:
    raise NotImplementedError


@dataclass
class Monkey:
    num: int
    operation: Callable[[int], int] = _fake_operation
    test_fn: Callable[[int], bool] = _fake_test
    send_to_true: int = 0
    send_to_false: int = 0
    holding_item_worry_levels: list[int] = field(default_factory=list)
    monkey_business: int = 0

    def __repr__(self) -> str:
        return f"""
        Monkey {self.num}:
          Holding Items: {self.holding_item_worry_levels}
            If true, send to: {self.send_to_true}
            If false, send to: {self.send_to_false}
        """


def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    monkeys: dict[int, Monkey] = {}

    current_monkey: Monkey | None = None
    for line in lines:
        if (match := re.match(r"Monkey (\d+):$", line)) is not None:
            num = int(match.group(1))
            current_monkey = Monkey(num)
            monkeys[num] = current_monkey
        elif (match := re.match(r"  Starting items: (.+)", line)) is not None:
            assert current_monkey
            current_monkey.holding_item_worry_levels = list(
                map(lambda i: int(i), match.group(1).split(", "))
            )
        elif (match := re.match(r"  Operation: new = (.+)", line)) is not None:
            assert current_monkey
            current_monkey.operation = _parse_operation(match.group(1))
        elif (match := re.match(r"  Test: divisible by (\d+)", line)) is not None:
            assert current_monkey
            div_num = int(match.group(1))
            current_monkey.test_fn = _parse_test(div_num)
        elif (
            match := re.match(r"    If true: throw to monkey (\d+)", line)
        ) is not None:
            assert current_monkey
            current_monkey.send_to_true = int(match.group(1))
        elif (
            match := re.match(r"    If false: throw to monkey (\d+)", line)
        ) is not None:
            assert current_monkey
            current_monkey.send_to_false = int(match.group(1))
        elif re.match(r"$", line) is not None:
            pass
        else:
            raise AssertionError(line)

    for _ in range(_NUMBER_OF_ROUNDS):
        for monkey_num in range(len(monkeys)):
            current_monkey = monkeys[monkey_num]

            for worry_level in current_monkey.holding_item_worry_levels:
                new_worry_level = current_monkey.operation(worry_level)
                new_worry_level = math.floor(new_worry_level / 3)

                test_result = current_monkey.test_fn(new_worry_level)

                send_to_monkey_num = (
                    current_monkey.send_to_true
                    if test_result
                    else current_monkey.send_to_false
                )

                monkeys[send_to_monkey_num].holding_item_worry_levels.append(
                    new_worry_level
                )

            current_monkey.monkey_business += len(
                current_monkey.holding_item_worry_levels
            )

            current_monkey.holding_item_worry_levels.clear()

    monkey_businesses = sorted(
        (m.monkey_business for m in monkeys.values()), reverse=True
    )

    print(monkey_businesses[0] * monkey_businesses[1])


_NUMBER_OF_ROUNDS = 20


def _parse_operation(op_str: str) -> Callable[[int], int]:
    ident1, sign, ident2 = op_str.split(" ")
    if sign == "+":

        def _add(i: int):
            a = i if ident1 == "old" else int(ident1)
            b = i if ident2 == "old" else int(ident2)
            return a + b

        return _add
    elif sign == "*":

        def _multiply(i: int):
            a = i if ident1 == "old" else int(ident1)
            b = i if ident2 == "old" else int(ident2)
            return a * b

        return _multiply
    else:
        raise AssertionError(sign)


def _parse_test(div_num: int) -> Callable[[int], bool]:
    def _test(i: int) -> bool:
        return i % div_num == 0

    return _test


if __name__ == "__main__":
    main()
