def main():
    with open("input.txt", "r") as f:
        lines = f.read()

    cs: list[str | None] = [None] * 4

    for i, c in enumerate(lines):
        cs.pop(0)
        cs.append(c)

        if all(cs):
            if len(frozenset(cs)) == len(cs):
                print(i + 1)
                break


if __name__ == "__main__":
    main()
