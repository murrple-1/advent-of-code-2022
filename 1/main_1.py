def main():
    elf_calories = []

    with open("input.txt", "r") as f:
        current_calory_total = 0
        for line in (l.rstrip("\n") for l in f.readlines()):
            if not line:
                elf_calories.append(current_calory_total)
                current_calory_total = 0
            else:
                current_calory_total += int(line)

        elf_calories.append(current_calory_total)

    print(max(elf_calories))


if __name__ == "__main__":
    main()
