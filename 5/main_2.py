import re


def main():
    lines: list[str]
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    split_index: int
    for i, line in enumerate(lines):
        if line == "":
            split_index = i
            break
    else:
        raise Exception

    stack_count = max(int(n) for n in re.findall(r"\d+", lines[split_index - 1]))
    stacks = [[] for _ in range(stack_count)]

    for line in reversed(lines[0 : split_index - 1]):
        for i, match in enumerate(re.findall(r"(   |\[[A-Z]\]) ?", line)):
            if match == "   ":
                pass
            else:
                char_match = re.match(r"\[([A-Z])\]", match)
                assert char_match
                stacks[i].append(char_match.group(1))

    for line in lines[split_index + 1 :]:
        match = re.match(r"move (\d+) from (\d+) to (\d+)", line)
        assert match
        move_count = int(match.group(1))
        from_stack_index = int(match.group(2)) - 1
        to_stack_index = int(match.group(3)) - 1

        temp_stack = []

        for _ in range(move_count):
            temp_stack.append(stacks[from_stack_index].pop())

        temp_stack.reverse()

        stacks[to_stack_index].extend(temp_stack)

    print("".join(s[-1] for s in stacks))


if __name__ == "__main__":
    main()
