def main():
    with open("input.txt", "r") as f:
        overlaps = 0
        for line in f.read().splitlines():
            first_range_str, second_range_str = line.split(",")

            first_range_start_str, first_range_end_str = first_range_str.split("-")
            second_range_start_str, second_range_end_str = second_range_str.split("-")

            first_range_start, first_range_end = int(first_range_start_str), int(
                first_range_end_str
            )
            second_range_start, second_range_end = int(second_range_start_str), int(
                second_range_end_str
            )

            first_range = frozenset(range(first_range_start, first_range_end + 1, 1))
            second_range = frozenset(range(second_range_start, second_range_end + 1, 1))

            if len(first_range.intersection(second_range)):
                overlaps += 1

        print(overlaps)


if __name__ == "__main__":
    main()
