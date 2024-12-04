def window_by_2(
    lst: list[int], acc: list[tuple[int, int]] = None
) -> list[tuple[int, int]]:
    if acc is None:
        acc = []

    if len(lst) == 1:
        return acc

    left = lst.pop(0)
    acc.append((left, lst[0]))
    return window_by_2(lst, acc)


def is_safe(diff: list[int]) -> bool:
    inc = diff[0] > 0

    for d in diff:
        if (inc and d < 0) or (not inc and d > 0) or d > 3 or d < -3 or d == 0:
            return False
    return True


def part1(inp: str):
    levels = [list(map(lambda i: int(i), l.split())) for l in inp.splitlines()]
    diff = [
        int(is_safe([d1 - d2 for d1, d2 in window_by_2(level)])) for level in levels
    ]

    return sum(diff)


def part2(inp: str):
    def dampen(level: list[int]) -> bool:
        for idx in range(len(level)):
            new_level = level.copy()
            new_level.pop(idx)
            diff = [d1 - d2 for d1, d2 in window_by_2(new_level)]

            if is_safe(diff):
                return True

        return False

    count = 0
    levels = [list(map(lambda i: int(i), l.split())) for l in inp.splitlines()]
    diff = [[d1 - d2 for d1, d2 in window_by_2(level.copy())] for level in levels]

    for idx, d in enumerate(diff):
        if not is_safe(d):
            count += int(dampen(levels[idx]))
        else:
            count += 1

    return count


if __name__ == "__main__":
    with open("./inputs/d2input.txt", "r") as f:
        inp = f.read()
        print(part1(inp))
        print(part2(inp))
