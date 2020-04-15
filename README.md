# Game of Life
A borderless implementation of the Game of Life cellular automaton.

**Code:**

```python
    from collections import defaultdict

    def GameOfLife(universe):
        """Performs a single iteration of Game of Life in a borderless universe."""

        neighbors    = defaultdict(int)
        neighborhood = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
        
        for (x,y) in universe:
            for (dx,dy) in neighborhood:
                neighbors[(x+dx,y+dy)] += 1

        new = set()
        for cell,n in neighbors.items():
            if n == 3 or (n == 2 and cell in universe): new.add(cell)

        return new

    def read(pattern, living='O', delta=(0,0)):
        """Reads a plaintext pattern and return its set of living cells."""

        universe = set()
        for y,row in enumerate(reversed(pattern)):
            for x,cell in enumerate(row):
                if cell == living: universe.add((x+delta[0],y+delta[1]))

        return universe
        
    def show(universe, (X,Y)):
        """Prints a rectangular portion of the universe on the screen."""

        length = 2*(X[1]-X[0]) + 1
        print('╔'+ '═'*length + '╗')
        for y in reversed(range(*Y)):
            row = ' '.join('■' if (x,y) in universe else ' ' for x in range(*X))
            print('║ ' + row  + ' ║')
        print('╚' + '═'*length + '╝')
```

**Example:**

```python
    try: input = raw_input  # Python 2
    except NameError: pass  # Python 3

    # Read the set of living cells from plaintext -- https://xkcd.com/2293/
    universe = read(("..OOO..",
                     "..O.O..",
                     "..O.O..",
                     "...O...",
                     "O.OOO..",
                     ".O.O.O.",
                     "...O..O",
                     "..O.O..",
                     "..O.O.."))

    # The visible universe: (x_range, y_range)
    window = ((-3,10), (-3,15))                 

    # Press Ctrl+C to exit:
    while(True):
        show(universe, window)
        universe = GameOfLife(universe)
        stop = input("\nPress <Return> to perform a step.")
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

