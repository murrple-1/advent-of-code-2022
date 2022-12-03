def main():
    with open("input.txt", "r") as f:
        total = 0

        lines = f.read().splitlines()
        for i in range(0, len(lines), 3):
            items1 = frozenset(lines[i])
            items2 = frozenset(lines[i + 1])
            items3 = frozenset(lines[i + 2])

            for char in items1.intersection(items2).intersection(items3):
                char_code = ord(char)

                if 65 <= char_code <= 90:
                    total += char_code - 64 + 26
                else:
                    total += char_code - 96

        print(total)


if __name__ == "__main__":
    main()
