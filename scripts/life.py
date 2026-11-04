import random
import re
from pathlib import Path

ROWS, COLS = 18, 40
README = Path(__file__).resolve().parent.parent / "README.md"
ALIVE, DEAD = "🟩", "⬛"


def parse(block):
    grid = [[c == ALIVE for c in line] for line in block.splitlines() if line and set(line) <= {ALIVE, DEAD}]
    gen = re.search(r"Generation: \*\*(\d+)\*\*", block)
    return (grid, int(gen.group(1))) if len(grid) == ROWS and gen else (None, 0)


def step(g):
    def n(r, c):
        return sum(g[(r + i) % ROWS][(c + j) % COLS] for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j)
    return [[(n(r, c) == 3) or (g[r][c] and n(r, c) == 2) for c in range(COLS)] for r in range(ROWS)]


def fresh():
    return [[random.random() < 0.28 for _ in range(COLS)] for _ in range(ROWS)]


text = README.read_text(encoding="utf-8")
m = re.search(r"<!-- LIFE-START -->(.*?)<!-- LIFE-END -->", text, re.S)
grid, gen = parse(m.group(1))
if grid is None:
    grid, gen = fresh(), 1
else:
    nxt = step(grid)
    if sum(map(sum, nxt)) == 0 or nxt == grid or step(nxt) == grid:
        grid, gen = fresh(), 1
    else:
        grid, gen = nxt, gen + 1

rows = "\n".join("".join(ALIVE if c else DEAD for c in r) for r in grid)
pop = sum(map(sum, grid))
block = f"\n```\n{rows}\n```\n\nGeneration: **{gen}** | Population: **{pop}**/{ROWS * COLS}\n"
README.write_text(text[: m.start(1)] + block + text[m.end(1):], encoding="utf-8")
