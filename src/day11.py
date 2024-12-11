import functools
from math import floor, log10


@functools.cache
def getNext(n: int, depth: int) -> int:
    if depth == 0:
        return 1
    elif n == 0:
        return getNext(1, depth - 1)

    exp = floor(log10(n))

    if exp % 2 == 1:
        scale = 10 ** ((exp + 1) // 2)
        return getNext(n // scale, depth - 1) + getNext(n % scale, depth - 1)
    else:
        return getNext(n * 2024, depth - 1)


def solve(inp: str, is_part2: bool) -> int:
    awnser = 0
    depth = 25 if not is_part2 else 75

    for n in inp.split():
        awnser += getNext(int(n), depth)
    return awnser


with open("inputs/d11input.txt") as f:
    inp = f.read().strip()
    print(f"Part 1: {solve(inp, False)}")
    print(f"Part 2: {solve(inp, True)}")
