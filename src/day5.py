def isCorrect(line: list[str], orders: list[str]) -> bool:
    curr = []
    for el in line:
        if (
            el in orders and not any(e in curr for e in orders[el])
        ) or el not in orders:
            curr.append(el)
    return curr == line


def part1(inp: str) -> int:
    result = 0
    sep = inp.index("\n\n")
    orders = {}

    for o in inp[:sep].splitlines():
        x, y = o.split("|")

        if x not in orders:
            orders[x] = [y]
        else:
            orders[x].append(y)

    updates = [l.split(",") for l in inp[sep + 2 :].splitlines()]

    for update in filter(lambda x: isCorrect(x, orders), updates):
        result += int(update[len(update) // 2])

    return result


def part2(inp: str) -> int:
    result = 0
    sep = inp.index("\n\n")
    orders = {}
    inv = {}

    for o in inp[:sep].splitlines():
        x, y = o.split("|")

        if y not in inv:
            inv[y] = [x]
        else:
            inv[y].append(x)

        if x not in orders:
            orders[x] = [y]
        else:
            orders[x].append(y)

    updates = [l.split(",") for l in inp[sep + 2 :].splitlines()]

    for update in filter(lambda x: not isCorrect(x, orders), updates):
        while not isCorrect(update, orders):
            line = []
            idx = 0
            while update:
                el = update.pop(0)
                line.append(el)

                if el in inv:
                    for b in filter(lambda x: x in update, inv[el]):
                        line.insert(idx, b)
                        update.remove(b)

                idx += 1
            update = line

        assert isCorrect(update, orders)
        result += int(line[len(line) // 2])

    return result


if __name__ == "__main__":
    with open("inputs/d5input.txt") as f:
        inp = f.read()
        print(f"Part 1: {part1(inp)}")
        print(f"Part 2: {part2(inp)}")
