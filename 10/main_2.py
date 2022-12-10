import sys


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

    for i in range(6):
        for j in range(40):
            value = x_register_values[(i * 40) + j]
            if value - 1 < j + 1 < value + 1:
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")

        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
