def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    x_register_values: list[int] = []
    current_value = 1

    for line in lines:
        line_parts = line.split(" ")

        if line_parts[0] == "noop":
            x_register_values.append(current_value)
        elif line_parts[0] == "addx":
            add = int(line_parts[1])
            x_register_values.extend([current_value, current_value])
            current_value += add
        else:
            raise AssertionError

    relevant_values: list[tuple[int, int]] = []

    for index in _RELEVANT_INDEXS:
        relevant_values.append((index, x_register_values[index - 1]))

    print(sum((index * value) for index, value in relevant_values))


_RELEVANT_INDEXS: list[int] = [20, 60, 100, 140, 180, 220]

if __name__ == "__main__":
    main()
