from typing import TypeVar

T = TypeVar("T")

List2d = list[list[T]]


def isInBound(coord: tuple[int, int], bound: tuple[int, int]) -> bool:
    x, y = coord
    width, height = bound

    return x >= 0 and x < width and y >= 0 and y < height


def part1(inp: str) -> int:
    def findPossibleCombination(
        coord: tuple[int, int], bound: tuple[int, int]
    ) -> List2d[int]:
        x, y = coord

        ret = [
            [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)],
            [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)],
            [(x, y), (x + 1, y + 1), (x + 2, y + 2), (x + 3, y + 3)],
            [(x, y), (x - 1, y - 1), (x - 2, y - 2), (x - 3, y - 3)],
            [(x, y), (x - 1, y + 1), (x - 2, y + 2), (x - 3, y + 3)],
        ]

        return list(filter(lambda l: all(map(lambda el: isInBound(el, bound), l)), ret))

    count = 0
    matrix: List2d[str] = [list(l.strip()) for l in inp.splitlines()]
    bound = (len(matrix[1]), len(matrix))

    for y, line in enumerate(matrix):
        for x, _ in enumerate(line):
            found = False

            for comb in findPossibleCombination((x, y), bound):
                s = "".join(list(map(lambda coord: matrix[coord[1]][coord[0]], comb)))
                if "XMAS" in [s, s[::-1]]:
                    count += 1

            if not found:
                matrix[y][x] = "."
    return count


def part2(inp: str) -> int:
    def findPossibleCombination(
        coord: tuple[int, int], bound: tuple[int, int]
    ) -> list[tuple[int]]:
        x, y = coord
        ret = [(x, y), (x + 2, y), (x + 1, y + 1), (x, y + 2), (x + 2, y + 2)]

        if all(map(lambda coor: isInBound(coor, bound), ret)):
            return ret
        else:
            return []

    matrix: List2d[str] = [list(l.strip()) for l in inp.splitlines()]
    bound = (len(matrix[1]), len(matrix))
    count = 0
    final = [["M", "S", "A", "M", "S"], ["S", "S", "A", "M", "M"]]

    for y, line in enumerate(matrix):
        for x, _ in enumerate(line):
            coord = findPossibleCombination((x, y), bound)
            if not coord:
                continue

            mas = list(map(lambda c: matrix[c[1]][c[0]], coord))

            if mas in final or mas[::-1] in final:
                count += 1

    return count


if __name__ == "__main__":
    with open("inputs/d4input.txt") as f:
        inp = f.read()
        print(f"Part 1: {part1(inp)}")
        print(f"Part 2: {part2(inp)}")
