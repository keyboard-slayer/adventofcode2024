import multiprocessing
from typing import Optional
from copy import deepcopy
from functools import partial

Coord = tuple[int, int]


def generateDirections(
    start: Coord,
    delta: Coord,
    bound: int,
    obs: list[Coord],
) -> list[Coord]:
    ret = []
    start_x, start_y = start
    x, y = delta

    while True:
        next_pos = (start_x + x, start_y + y)
        if next_pos in obs:
            return (False, ret)
        elif (next_pos[0] >= bound or next_pos[0] < 0) or (
            next_pos[1] >= bound or next_pos[1] < 0
        ):
            ret.append(next_pos)
            return (True, ret)
        else:
            start_x += x
            start_y += y
            ret.append(next_pos)


def solve(
    matrix: list[list[str]], guard: Coord, obs: list[Coord], bound: int
) -> Optional[list[Coord]]:
    visited = []
    ret = []
    while True:
        match matrix[guard[1]][guard[0]]:
            case "^":
                direct = ">"
                delta = (0, -1)
            case ">":
                direct = "v"
                delta = (1, 0)
            case "v":
                direct = "<"
                delta = (0, 1)
            case "<":
                direct = "^"
                delta = (-1, 0)

        oob, pos = generateDirections(guard, delta, bound, obs)

        if not pos:
            pos = [guard]
        elif pos in visited:
            return None
        else:
            ret += pos[:-1] + [guard]

        visited.append(pos)
        guard = pos[-1]

        if oob:
            return set(ret)

        matrix[pos[-1][1]][pos[-1][0]] = direct


def part1(inp: str) -> int:
    grid = [list(l) for l in inp.splitlines()]

    inp = inp.replace("\n", "")
    idx_guard = inp.index("^")
    bound = len(grid)
    guard = (idx_guard % bound, idx_guard // bound)
    obs = [(idx % bound, idx // bound) for idx, o in enumerate(inp) if o == "#"]
    return len(solve(grid, guard, obs, bound))


def process(
    path: Coord,
    grid: list[list[str]],
    guard: Coord,
    obs: list[Coord],
    bound: int,
    res: list[int],
):
    answer = 0

    if path == guard:
        return 0

    tmpObs = obs.copy()
    tmpObs.append(path)
    newGrid = deepcopy(grid)

    if solve(newGrid, guard, tmpObs, bound) is None:
        answer += 1
    return answer


def part2(inp: str) -> int:
    res = 0
    grid = [list(l) for l in inp.splitlines()]

    inp = inp.replace("\n", "")
    idx_guard = inp.index("^")
    bound = len(grid)
    guard = (idx_guard % bound, idx_guard // bound)
    obs = [(idx % bound, idx // bound) for idx, o in enumerate(inp) if o == "#"]
    path = solve(deepcopy(grid), guard, obs, bound)

    res = []
    func = partial(process, grid=grid, guard=guard, obs=obs, bound=bound, res=res)
    pool = multiprocessing.Pool(int(multiprocessing.cpu_count() * 1.8))

    res = pool.map(func, path)
    return sum(res)


if __name__ == "__main__":
    with open("inputs/d6input.txt") as f:
        inp = f.read()
        print(f"Part 1: {part1(inp)}")
        print(f"Part 2: {part2(inp)}")
