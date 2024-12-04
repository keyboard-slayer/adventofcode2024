import re
import functools


def part1(s: str) -> int:
    return sum(
        [
            functools.reduce(
                lambda a, b: int(a) * int(b),
                n.replace("mul(", "").replace(")", "").split(","),
            )
            for n in re.findall(r"mul\(\d{1,3},\d{1,3}\)", s)
        ]
    )


def part2(s: str) -> int:
    return part1(
        "".join(
            filter(
                lambda l: not l.startswith("don't()"),
                s.replace("do()", "\ndo()").replace("don't()", "\ndon't()").split("\n"),
            ),
        )
    )


if __name__ == "__main__":
    with open("./inputs/d3input.txt", "r") as f:
        mem = f.read().replace("\n", "")
        print(part1(mem))
        print(part2(mem))
