def solve(inp: str, is_part2: bool):
    def findTrail(node: tuple[int, int], grid: list[list[str]], visited=None):
        x, y = node
        height = int(grid[y][x])
        count = 0

        if height == 9:
            return count + 1

        if visited is None:
            visited = []

        nodes = [n for n in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]]

        for n in nodes:
            if (
                0 <= n[0] < len(grid[0])
                and 0 <= n[1] < len(grid)
                and grid[n[1]][n[0]] == str(height + 1)
                and (n not in visited or is_part2)
            ):
                visited.append(n)
                count += findTrail(n, grid, visited)

        return count

    grid = [list(line) for line in inp.splitlines()]

    routes = [
        (idx % len(grid), idx // len(grid))
        for idx, z in enumerate(inp.replace("\n", ""))
        if z == "0"
    ]

    count = 0
    for n in routes:
        sz = findTrail(n, grid)
        count += sz

    return count


if __name__ == "__main__":
    with open("inputs/d10input.txt") as f:
        inp = f.read().strip()
        print(f"Part 1: {solve(inp, False)}")
        print(f"Part 2: {solve(inp, True)}")
