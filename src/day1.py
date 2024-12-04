def part1(inp: str) -> int:
    lines = [list(map(lambda x: int(x), i.split())) for i in inp.splitlines()]
    left, right = [el[0] for el in lines], [el[1] for el in lines]
    count = 0

    while left:
        l = min(left)
        left.remove(l)

        r = min(right)
        right.remove(r)
        count += abs(r - l)

    return count


def part2(inp: str) -> int:
    lines = [list(map(lambda x: int(x), i.split())) for i in inp.splitlines()]
    left, right = [el[0] for el in lines], [el[1] for el in lines]
    count = 0

    while left:
        l = left.pop(0)
        rs = [idx for idx, el in enumerate(right) if el == l]
        r = len(rs)
        count += l * r

        for idx in rs[::-1]:
            right.pop(idx)

    return count


if __name__ == "__main__":
    with open("./inputs/d1input.txt", "r") as f:
        inp = f.read()
        print(part1(inp))
        print(part2(inp))
