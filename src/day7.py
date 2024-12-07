from itertools import product


def solve(inp: str, lops: list[callable]) -> int:
    lines = inp.splitlines()
    result = 0

    for l in lines:
        resp, terms = l.split(":")

        terms = [int(i) for i in terms.strip().split()]
        operators = list(
            product(
                lops,
                repeat=len(terms) - 1,
            )
        )

        for ops in operators:
            answer = terms[0]
            for idx, op in enumerate(ops):
                answer = op(answer, terms[idx + 1])
            if answer == int(resp):
                result += answer
                break
    return result


with open("inputs/d7input.txt") as f:
    inp = f.read()

    print(f"Part 1: {solve(inp, [
                    lambda x, y: x + y,
                    lambda x, y: x * y])}")

    print(f"Part 2: {solve(inp, [
                    lambda x, y: x + y,
                    lambda x, y: x * y,
                    lambda x, y: int(str(x) + str(y))])}")
