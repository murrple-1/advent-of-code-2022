def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    all_pos: list[tuple[int, int]] = [(0, 0)] * 10

    tail_visited: set[tuple[int, int]] = set([all_pos[-1]])

    for line in lines:
        dir_, steps_str = line.split(" ")
        steps = int(steps_str)

        for i in range(steps):
            if dir_ == "U":
                all_pos[0] = all_pos[0][0], all_pos[0][1] - 1
            elif dir_ == "D":
                all_pos[0] = all_pos[0][0], all_pos[0][1] + 1
            elif dir_ == "L":
                all_pos[0] = all_pos[0][0] - 1, all_pos[0][1]
            elif dir_ == "R":
                all_pos[0] = all_pos[0][0] + 1, all_pos[0][1]
            else:
                raise AssertionError

            for j, non_head_pos in enumerate(all_pos[1:]):
                all_pos[j + 1] = _tail_chase(all_pos[j], all_pos[j + 1])

            tail_visited.add(all_pos[-1])

    print(len(tail_visited))


def _tail_chase(
    head_pos: tuple[int, int], old_tail_pos: tuple[int, int]
) -> tuple[int, int]:
    head_x, head_y = head_pos
    old_tail_x, old_tail_y = old_tail_pos

    if abs(head_x - old_tail_x) <= 1 and abs(head_y - old_tail_y) <= 1:
        return old_tail_x, old_tail_y

    if head_x > old_tail_x:
        if head_y > old_tail_y:
            return old_tail_x + 1, old_tail_y + 1
        elif head_y < old_tail_y:
            return old_tail_x + 1, old_tail_y - 1
        else:
            return old_tail_x + 1, old_tail_y
    elif head_x < old_tail_x:
        if head_y > old_tail_y:
            return old_tail_x - 1, old_tail_y + 1
        elif head_y < old_tail_y:
            return old_tail_x - 1, old_tail_y - 1
        else:
            return old_tail_x - 1, old_tail_y
    else:
        if head_y > old_tail_y:
            return old_tail_x, old_tail_y + 1
        elif head_y < old_tail_y:
            return old_tail_x, old_tail_y - 1
        else:
            raise RuntimeError(f"{head_x}, {head_y} vs {old_tail_x}, {old_tail_y}")


if __name__ == "__main__":
    main()
