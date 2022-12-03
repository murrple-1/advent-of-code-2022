def main():
    with open("input.txt", "r") as f:
        total = 0
        for line in f.read().splitlines():
            line_length = len(line)

            comp1 = frozenset(line[0 : int(line_length / 2)])
            comp2 = frozenset(line[int(line_length / 2) :])

            for char in comp1.intersection(comp2):
                char_code = ord(char)

                if 65 <= char_code <= 90:
                    total += char_code - 64 + 26
                else:
                    total += char_code - 96

        print(total)


if __name__ == "__main__":
    main()
