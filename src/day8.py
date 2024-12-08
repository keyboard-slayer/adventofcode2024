import itertools

Coord = tuple[int, int]


def antiAntennaPos(coords: tuple[Coord, Coord]) -> tuple[Coord, Coord]:
    return (
        (coords[0][0] - coords[1][0], coords[0][1] - coords[1][1]),
        (coords[1][0] - coords[0][0], coords[1][1] - coords[0][1]),
    )


def addPos(coord: Coord, delta: Coord) -> Coord:
    return (coord[0] + delta[0], coord[1] + delta[1])


def inMatrix(coord: Coord, matrix: list[list[str]]) -> bool:
    x, y = coord
    return -1 < x < len(matrix[0]) and -1 < y < len(matrix)


def part1(inp: str) -> int:
    answer = 0
    matrix = []
    antenna: dict[tuple[int, int]] = {}

    for y, line in enumerate(inp.splitlines()):
        matrix.append(list(line))
        for x, el in enumerate(line):
            if el != ".":
                if el in antenna:
                    antenna[el].append((x, y))
                else:
                    antenna[el] = [(x, y)]

    antenna = {
        k: list(itertools.combinations(antenna[k], r=2))
        if len(antenna[k]) > 1
        else antenna[k]
        for k in antenna.keys()
    }

    for a in antenna.keys():
        if len(antenna[a]) > 1:
            for points in antenna[a]:
                p1, p2 = antiAntennaPos(points)
                x, y = addPos(points[0], p1)

                if inMatrix((x, y), matrix) and matrix[y][x] not in [a, "#"]:
                    answer += 1
                    matrix[y][x] = "#"

                x, y = addPos(points[1], p2)

                if inMatrix((x, y), matrix) and matrix[y][x] not in [a, "#"]:
                    answer += 1
                    matrix[y][x] = "#"

    return answer


def part2(inp: str) -> int:
    answer = []
    matrix = []
    antenna: dict[tuple[int, int]] = {}

    for y, line in enumerate(inp.splitlines()):
        matrix.append(list(line))
        for x, el in enumerate(line):
            if el != ".":
                if el in antenna:
                    antenna[el].append((x, y))
                else:
                    antenna[el] = [(x, y)]

    antenna = {
        k: list(itertools.combinations(antenna[k], r=2))
        if len(antenna[k]) > 1
        else antenna[k]
        for k in antenna.keys()
    }

    for a in antenna.keys():
        if len(antenna[a]) > 1:
            for points in antenna[a]:
                p, _ = antiAntennaPos(points)
                answer.append(points[0])

                i = 1
                while True:
                    ant = (points[0][0] + p[0] * i, points[0][1] + p[1] * i)
                    if not inMatrix(ant, matrix):
                        break
                    answer.append(ant)
                    i += 1

                i = -1
                while True:
                    ant = (points[0][0] + (p[0] * i), points[0][1] + (p[1] * i))
                    if not inMatrix(ant, matrix):
                        break
                    answer.append(ant)
                    i -= 1

    return len(set(answer))


if __name__ == "__main__":
    with open("inputs/d8input.txt") as f:
        inp = f.read().strip()
        print(f"Part 1: {part1(inp)}")
        print(f"Part 2: {part2(inp)}")
