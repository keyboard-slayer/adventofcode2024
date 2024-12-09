from dataclasses import dataclass


def part1(inp: str):
    n = 0
    rep = []
    idx = 0
    scount = 0

    for i, el in enumerate(inp):
        if i % 2 == 0:
            rep += [str(n) for _ in range(int(el))]
            scount += int(el)
            idx += int(el)
            n += 1
        else:
            rep += "." * int(el)

    end = len(rep)
    answer = 0

    lastDot = len(rep) if "." not in rep else len(rep) - rep[::-1].index(".")

    for idx, r in enumerate(rep[:lastDot]):
        if idx == end:
            break

        while r == ".":
            end -= 1
            r = rep[end]

        if end < scount:
            break

        answer += idx * int(r)
    return answer


@dataclass
class Node:
    start: int
    len: int

    def __lt__(self, other):
        return self.start < other.start


def part2(inp):
    freelist: list[Node] = []
    filelist: list[Node] = []
    length = 0

    for i, el in enumerate(inp):
        if int(el):
            node = Node(length, int(el))
            if i % 2 == 0:
                filelist.append(node)
            else:
                freelist.append(node)
            length += int(el)

    for i, f in enumerate(filelist[::-1]):
        idx = len(filelist) - 1 - i

        spots = sorted([n for n in freelist if n.len >= f.len])

        if not spots:
            continue

        spot = spots[0]

        if spot.start > f.start:
            continue

        freelist.append(Node(f.start, f.len))
        f.start = spot.start
        filelist[idx] = f

        spotIdx = freelist.index(spot)
        spot.start += f.len
        spot.len -= f.len

        if spot.len > 0:
            freelist[spotIdx] = spot

    answer = 0
    for idx, n in enumerate(filelist):
        answer += sum([n * idx for n in range(n.start, n.len + n.start)])
    return answer


if __name__ == "__main__":
    with open("inputs/d9input.txt") as f:
        inp = f.read().strip()
        print(f"Part 1: {part1(inp)}")
        print(f"Part 2: {part2(inp)}")
