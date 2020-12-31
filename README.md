# Game of Life
A minimalist implementation of the Game of Life cellular automaton.

**Code:**

```python
from collections import defaultdict

def next_GameOfLife(universe):
    """Performs a single iteration of Game of Life in a boundless universe."""

    candidates = defaultdict(int)
    for (x,y) in universe:
        for (dx,dy) in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
            candidates[(x+dx,y+dy)] += 1

    new_universe = set()
    for cell, neighbors in candidates.items():
        if neighbors == 3 or (neighbors == 2 and cell in universe):
            new_universe.add(cell)

    return new_universe

def read_GameOfLife(pattern, living='O'):
    """Reads a pattern and return its set of living cells."""

    universe = set()
    for y,row in enumerate(reversed(pattern)):
        for x,cell in enumerate(row):
            if cell == living: universe.add((x,y))

    return universe

def show_GameOfLife(universe, X, Y):
    """Prints a rectangular window of the universe on the screen."""

    print('╔'+'═'*(2*(X[1]-X[0])+1)+'╗')
    for y in reversed(range(*Y)):
        print('║ '+' '.join(' ■'[(x,y) in universe] for x in range(*X))+' ║')
    print('╚'+'═'*(2*(X[1]-X[0])+1)+'╝')
```

**Example:**

```python
# Read the set of living cells from plaintext -- https://xkcd.com/2293/
universe = read_GameOfLife(("..OOO..",
                            "..O.O..",
                            "..O.O..",
                            "...O...",
                            "O.OOO..",
                            ".O.O.O.",
                            "...O..O",
                            "..O.O..",
                            "..O.O.."))

# Press Ctrl+C to exit
while(True):
    show_GameOfLife(universe, (-3,10), (-3,15))
    universe = next_GameOfLife(universe)
    stop     = input("\nPress <Return> to perform a step.")
    print("\x1b[1A\x1b[2K\x1b[1A\x1b[2K\x1b[1A")
    if stop: break
```

**Output:**

    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║           ■ ■ ■           ║
    ║           ■   ■           ║
    ║           ■   ■           ║
    ║             ■             ║
    ║       ■   ■ ■ ■           ║
    ║         ■   ■   ■         ║
    ║             ■     ■       ║
    ║           ■   ■           ║
    ║           ■   ■           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║             ■             ║
    ║           ■   ■           ║
    ║         ■ ■   ■ ■         ║
    ║           ■   ■           ║
    ║         ■                 ║
    ║         ■                 ║
    ║         ■       ■         ║
    ║             ■   ■         ║
    ║           ■   ■ ■         ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║             ■             ║
    ║         ■ ■   ■ ■         ║
    ║         ■ ■   ■ ■         ║
    ║           ■   ■ ■         ║
    ║         ■ ■               ║
    ║       ■ ■ ■               ║
    ║           ■   ■           ║
    ║           ■ ■   ■ ■       ║
    ║             ■ ■ ■         ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║           ■ ■ ■           ║
    ║         ■       ■         ║
    ║                   ■       ║
    ║               ■ ■         ║
    ║       ■                   ║
    ║       ■                   ║
    ║               ■ ■         ║
    ║           ■       ■       ║
    ║           ■ ■   ■ ■       ║
    ║               ■           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║             ■             ║
    ║           ■ ■ ■           ║
    ║           ■ ■ ■ ■         ║
    ║               ■   ■       ║
    ║                 ■         ║
    ║                           ║
    ║                           ║
    ║                 ■         ║
    ║           ■       ■       ║
    ║           ■ ■ ■ ■ ■       ║
    ║             ■ ■ ■         ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║           ■ ■ ■           ║
    ║                 ■         ║
    ║           ■               ║
    ║                   ■       ║
    ║                 ■         ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║           ■       ■       ║
    ║           ■       ■       ║
    ║           ■       ■       ║
    ║               ■           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║                           ║
    ║             ■             ║
    ║             ■ ■           ║
    ║           ■   ■           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║         ■ ■ ■   ■ ■ ■     ║
    ║             ■   ■         ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║                           ║
    ║             ■ ■           ║
    ║           ■   ■           ║
    ║               ■           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║           ■       ■       ║
    ║           ■ ■   ■ ■       ║
    ║             ■   ■         ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║                           ║
    ║             ■ ■           ║
    ║               ■ ■         ║
    ║             ■             ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║           ■ ■   ■ ■       ║
    ║           ■ ■   ■ ■       ║
    ║           ■ ■   ■ ■       ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║                           ║
    ║             ■ ■ ■         ║
    ║                 ■         ║
    ║               ■           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║           ■ ■   ■ ■       ║
    ║         ■           ■     ║
    ║           ■ ■   ■ ■       ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║               ■           ║
    ║               ■ ■         ║
    ║             ■   ■         ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║           ■       ■       ║
    ║         ■           ■     ║
    ║           ■       ■       ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║               ■ ■         ║
    ║             ■   ■         ║
    ║                 ■         ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║         ■ ■       ■ ■     ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║               ■ ■         ║
    ║                 ■ ■       ║
    ║               ■           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                           ║
    ║               ■ ■ ■       ║
    ║                   ■       ║
    ║                 ■         ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                 ■         ║
    ║                 ■ ■       ║
    ║               ■   ■       ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    ╔═══════════════════════════╗
    ║                           ║
    ║                 ■ ■       ║
    ║               ■   ■       ║
    ║                   ■       ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ║                           ║
    ╚═══════════════════════════╝
    
    Press <Return> to perform a step.

