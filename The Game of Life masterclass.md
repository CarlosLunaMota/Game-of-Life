# The Game of Life master class

**TL;DR:** This is a programming master class for Computer Science students. It highlights several interesting ideas that arose during the implementation of a Conway's Game of Life emulator. The examples are written in Python, but the basic ideas apply to any high level programming language.

## Conway's Game of Life

**John Horton Conway** (1937-2020) was an English mathematician who made notable contributions in many fields related with computer science. The best known of such contributions, although not the most relevant, is a cellular automaton called the Game of Life.

A **cellular automaton** consists of a regular N-dimensional grid of cells, each in one of a finite number of states. An initial configuration is selected by assigning a state to each cell. After that, the cells evolve according to some fixed rules that determine the new state of each cell in terms of the current state of the cell and the states of the cells in its neighborhood. Typically, the rules for updating the state of the cells are the same for each cell, don't change over time and are applied to the whole grid simultaneously in discrete time increments.

The cellular automata were originally discovered in the 1940s by **Stanislaw Ulam** and **John von Neumann**, but they were popularized by **Martin Gardner**'s articles about Conway's Game of Life in the 1970s. Nowadays, they still constitute an active research field that produces results not only in mathematics and computer science, but also in seemingly unrelated fields like biology or cosmology (see the works of **Stephen Wolfram**).

**Conway's Game of Life** is the most popular cellular automaton. It's _played_ in an infinite two-dimensional grid of square cells that can be in two states: alive or dead. Initially, only a finite set of cells (called the **seed**) is alive, and _the game_ consist in looking for initial seeds whose evolution, following the deterministic rules defined below, is interesting for some user-defined reason such as "grows indefinitely", "reaches an stationary state" or "simulates a Turing machine".

To determine the state of a cell after a discrete time increment (called a **tick**) we need to know the current state of the cell and its 8 neighbors (the set of cells that are orthogonally or diagonally adjacent to the cell):

 * Any live cell with fewer than two live neighbors dies, as if by underpopulation.
 * Any live cell with more than three live neighbors dies, as if by overpopulation.
 * Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
 * In all other cases, the cell remains in the same state.

These simple rules lead to a surprisingly complex emergent behavior that includes static patterns (called **still lifes**), periodic patterns (called **oscillators**), translating patterns (called **spaceships**), etc.

The Game of Life has fascinated thousands of programmers since the 1970's, as much so, that one of its most iconic patterns (called the **glider**) has become a universally recognized _hacker emblem_.

## Our task

All programming tasks should start by writing down the **specification**, an unambiguous contract that tells us what must be delivered. Believe it or not, misunderstanding (or ignoring) the specification is one of the main sources of problems of the computer programming field.

In this case, the specification seems quite straightforward:

 * **Task:** implement a function that updates the state of a Game of Life infinite grid.
 * **Input:** an arbitrary grid state defined by the user that must be considered read-only and shouldn't be modified.
 * **Output:** the new grid state that results from updating (one tick) the supplied grid state following the standard Game of Life updating rules.

The specification above doesn't tell us which format should we use to store the grid state, so we can assume that we can choose whichever format suits us best as long as it satisfies the rest of the specification. This implies, for example, that our format should be able to deal with arbitrarily big (albeit finite) inputs and outputs.

The specification doesn't say either if the input and output formats must be the equal, but it is safe to assume that this will be the best design choice for any reasonable use case. More in general, we don't know anything about how this function will be used, but all things being equal, the simpler the input/output format, the better.

Before continuing reading, think for a moment how would you implement this task or, even better, implement it in your favorite programming language.

## The classic approach

The first idea that came to my mind after reading the specification above was to use a two-dimensional array to store the grid state. To update the array you create an empty array of the same size, and then you scan the original array cell by cell (reading the information of the cell and its 8 neighbors) to determine the content of the new array. Something like this:

```python3
def next_GameOfLife(grid):
    rows, cols   = len(grid), len(grid[0])
    neighborhood = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

    new_grid = [[0 for c in range(cols)] for r in range(rows)]
    for r in range(rows):
        for c in range(cols):
            n = sum(grid[r+dr][c+dc] for (dr,dc) in neighborhood)
            if   grid[r][c] == 1 and 2 <= n <= 3: new_grid[r][c] = 1
            elif grid[r][c] == 0 and      n == 3: new_grid[r][c] = 1

    return new_grid
```

Unfortunately, this straighforward implementation doesn't work because it doesn't account for the special neighbor-counting cases at the edges. The simplest workaround for this issue is to make the input grid a little bit larger (adding an empty 2-cell border) and then just update and output the interior cells of that augmented grid:

```python3
def next_GameOfLife(universe):
    """Performs a single iteration of Game of Life in a boundless universe."""

    grid, origin = universe
    rows, cols   = len(grid)+4, len(grid[0])+4
    neighborhood = (0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)

    old_grid  = [[0 for c in range(cols)], [0 for c in range(cols)]]
    old_grid += [[0, 0] + row[:] + [0, 0] for row in grid]
    old_grid += [[0 for c in range(cols)], [0 for c in range(cols)]]

    new_grid = [[0 for c in range(cols-2)] for r in range(rows-2)]
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            n = sum(old_grid[r+dr][c+dc] for (dr,dc) in neighborhood)
            if   old_grid[r][c] == 1 and 2 <= n <= 3: new_grid[r-1][c-1] = 1
            elif old_grid[r][c] == 0 and      n == 3: new_grid[r-1][c-1] = 1

    return new_grid, (origin[0]-1, origin[1]-1)
```

This version is almost as simple as the previous one and satisfies the specification so, technically, we are done. However, enlarging the output size every single iteration is unacceptable for many foreseable use cases, so it is advisable to trim the output as much as possible:

```python3
def next_GameOfLife(universe):
    """Performs a single iteration of Game of Life in a boundless universe."""

    grid, origin = universe
    rows, cols   = len(grid)+4, len(grid[0])+4
    neighborhood = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

    old_grid  = [[0 for c in range(cols)], [0 for c in range(cols)]]
    old_grid += [[0, 0] + row[:] + [0, 0] for row in grid]
    old_grid += [[0 for c in range(cols)], [0 for c in range(cols)]]

    new_grid = [[0 for c in range(cols)] for r in range(rows)]
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            n = sum(old_grid[r+dr][c+dc] for (dr,dc) in neighborhood)
            if   old_grid[r][c] == 1 and 2 <= n <= 3: new_grid[r][c] = 1
            elif old_grid[r][c] == 0 and      n == 3: new_grid[r][c] = 1

    t, b = 1+all(new_grid[1][col] == 0 for col in range(cols)), rows-2
    while t < b and all(new_grid[b][col] == 0 for col in range(cols)): b -= 1
    while t < b and all(new_grid[t][col] == 0 for col in range(cols)): t += 1

    l, r = 1+all(new_grid[row][1] == 0 for row in range(rows)), cols-2
    while l < r and all(new_grid[row][r] == 0 for row in range(rows)): r -= 1
    while l < r and all(new_grid[row][l] == 0 for row in range(rows)): l += 1
    
    new_grid   = [row[l:r+1] for row in new_grid[t:b+1]]
    new_origin = (origin[0]+l-2, origin[1]+t-2)
    return new_grid, new_origin
```

Now the frame of reference might move in unpredictable ways from one iteration to the next one, so it is necessary to keep track of the coordinates of `grid[0][0]`.  This complicates the input/output format but in a reasonable way. Are we done, now?

Well, the implementation is no longer straightforward, and I would add some sanity checks for the input (do all rows of the grid have the same length?) and some edge-cases tests (what about empty grids?) just to convince myself that the code works as intended, but I don't think that I would go any further than that using this approach (you could save time and memory by dealing with the edges without copying the input grid but, since you have to allocate the output grid anyway, it won't make a huge difference).

Many programmers will deal with this task more or less like I had done so far, solving issues one by one until the code works well enough to be shipped. The result is, very often, a complex project with lots of subroutines and too many parameters settled to arbitrary values. When you find yourself wrestling with one of such projects, you should rejoice, because they are perfect opportunities to learn and grow as a programmer. Take a break, step away from your computer and think about what are you trying to accomplish. Very often, it will be a very different thing that what you were doing at that point.

## The sparse approach

The main issue with the previous approach was the use of a two-dimensional array to store a potentially infinite grid state. At first, it seemed a natural election for that purpose, but then we started to see its many shortcomings. The problem, here, is that we took that decision at the very beginning of our design process, and we just carried on solving issues one by one as we found them, without ever considering stepping back and taking a different path. Let's see what would happen if we take a moment to look for a better representation of our infinite grid.

**Observation 1:** The grid has an infinite number of dead cells but only a finite number of live cells.

When looking for a data structure it is important to understand the nature of our data. In this case, the key observation is that there  are many more dead cells than live cells. There are several contexts where this situation arises, and we can look at them to learn how to handle it.

One of such contexts is the sparse matrix representation used in numerical analysis. In many optimization problems, the numerical matrix that contains the instance data is overwhelmingly populated by zeros. It will be very wasteful to store these matrices as two-dimensional arrays and the common approach is to store a triplet `(row, column, value)` for each non-zero value. Since we are now explicitly storing information that was previously implicit (i.e. the `(row, column)` location of the non-zero values), this approach might end up requiring more memory that a simple two-dimensional array if the matrix is not sparse enough. However, using this format has the additional advantage of being able to iterate over the non-zero values while skipping large zero-filled regions of the matrix, and this might speed up the algorithm even if it increases its memory footprint.

In our case, the situation is even better: since the cells only have two possible states, we don't need to store their `value`, we only need to store the coordinates `(x,y)` of the live cells (always a finite number) and assume that all other cells are dead (a potentially infinite number).

Python has several containers that are able to store these `(x,y)` pairs, and we will choose among them depending on which additional operations we require from the container.

**Observation 2:** We don't need to update all the cells of the grid.

Now that we are dealing with an implicit infinite grid, it is impossible to check all its cells during the update operation as we did when we had a finite two-dimensional array. Fortunately, all but a finite set of cells will have no neighbors and, as a consequence, will be dead after the update. So we first generate a set of `candidates` with all the cells that have at least one neighbor:

```python3
def next_GameOfLife(universe):

    neighborhood = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

    candidates = set()
    for (x,y) in universe:
        for (dx,dy) in neighborhood:
            candidates.add((x+dx,y+dy))

    new_universe = set()
    for (x,y) in candidates:
        n = sum((x+dx,y+dy) in universe for (dx,dy) in neighborhood)
        if   (x,y)     in universe and 2 <= n <= 3: new_universe.add((x,y))
        elif (x,y) not in universe and      n == 3: new_universe.add((x,y))

    return new_universe
```

Note that we do not need to include the current live cells on the `candidates` set because, even if a cell is alive, it won't remain in that state unless it has, at least, 2 neighbors (and we just care about live cells now).

Note also that we are taking advantage of the "overwritting" feature of python's sets: we can safely include the same candidate several times (because it has more than one neighbor) and the data structure will take care of removing the repeated elements automatically.

Finally, we are also using python's sets to store the live cells because we need to perform a lot of inclusion tests, `(x,y) in universe`, and python's sets do them more efficiently than python's lists.

This implementation is more elegant, more capable and more efficient that the previous one, but there is room for improvement. Let's see how!

**Observation 3:** Python's `and` and `or` are short-circuit operators. They only evaluate the second argument when it is absolutely necessary.

The update rules for the **Game of Life** state that:

 * Any live cell with fewer than two live neighbors dies, as if by underpopulation.
 * Any live cell with more than three live neighbors dies, as if by overpopulation.
 * Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
 * In all other cases, the cell remains in the same state.

Since we only care about live cells, we are only using the ones that specify which cells will be alive in the next generation:

 * A live cell will be alive in the next generation if it has 2 or 3 live neighbors
 * A dead cell will be alive in the next generation if it has 3 live neighbors

Rewriting the rules like this, we can clearly see that it is always necessary to know the number of neighbors of a cell in order to decide if it is going to live after the update, but, very often (if the cell doesn't have 2 or 3 neighbors), it is not necessary to know anything about the cell itself:

 * A cell will be alive in the next generation if and only if it has 3 neighbors or (it has 2 neighbors and is currently live)

So we could avoid checking the current state of the cell unless it is absolutely necessary, and save some _relatively costly_ inclusion test, exploiting the short-circuit behavior of python's `and` and `or` operators.

```python3
def next_GameOfLife(universe):

    neighborhood = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

    candidates = set()
    for (x,y) in universe:
        for (dx,dy) in neighborhood:
            candidates.add((x+dx,y+dy))

    new_universe = set()
    for (x,y) in candidates:
        n = sum((x+dx,y+dy) in universe for (dx,dy) in neighborhood)
        if n == 3 or (n == 2 and (x,y) in universe): new_universe.add((x,y))

    return new_universe
```

**Observation 4:** We are checking the `neighborhood` twice!

If you look at the code above, it is evident that we are checking the `neighborhood` twice. First we check the neighborhood of the cells that are currently alive to generate the set of `candidates`. Then we check the neighborhood of each candidate to count how many neighbors does it have.

The first neighborhood scan is unavoidable: each live cell contributes to the neighbors count of all the candidates around it and the only way to avoid examining these alive-candidate relationships will be to discard candidates before counting how many neighbors they have (which is impossible, in general). But the second scan seems wasteful: we are doing _relatively costly_ inclusiong test that most of the time fail. Couldn't we perform both operations at the same time?

Of course we can! We relationships that we care about (i.e. the ones between cells that are currently alive and cells that might be alive in the next generation) are exactly the same in both cases, so we could just keep the count of how many live cells _vote_ for each candidate while we are building the `candidates` set.

```python3
def next_GameOfLife(universe):
    """Performs a single iteration of Game of Life in a boundless universe."""

    candidates = dict()
    for (x,y) in universe:
        for (dx,dy) in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
            if (x+dx,y+dy) in candidates: candidates[x+dx,y+dy] += 1
            else:                         candidates[x+dx,y+dy]  = 1

    new_universe = set()
    for cell, neighbors in candidates.items():
        if neighbors == 3 or (neighbors == 2 and cell in universe):
            new_universe.add(cell)

    return new_universe
```

Now we are using python's dictionaries for the `candidates` containers, so we can store additional information associated with each candidate (its number of neighbors). The pattern that we are using here, updating a dictionary entry if it exists or creating it if it doesn't, is so common that python has a specific data structure, `defaultdict`, in the `collections` module to do that in the most efficient way:

```python3
from collections import defaultdict

def next_GameOfLife(universe):
    """Performs a single iteration of Game of Life in a boundless universe."""

    candidates = defaultdict(int)
    for (x,y) in universe:
        for (dx,dy) in (0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1):
            candidates[x+dx,y+dy] += 1

    new_universe = set()
    for cell, neighbors in candidates.items():
        if neighbors == 3 or (neighbors == 2 and cell in universe):
            new_universe.add(cell)

    return new_universe
```

Now we only have to implement some helper functions:

```python3
def read_GameOfLife(pattern, origin=(0,0), alive='O'):
    """Reads a pattern and return its set of live cells."""

    universe = set()
    for y,row in enumerate(reversed(pattern)):
        for x,cell in enumerate(row):
            if cell == alive: universe.add((origin[0]+x, origin[1]+y))

    return universe

def show_GameOfLife(universe, x_range, y_range):
    """Prints a rectangular window of the universe on the screen."""

    print('╔' + '═' * (2*len(x_range) + 1) + '╗')
    for y in reversed(y_range):
        print('║ ' + ' '.join(' ■'[(x,y) in universe] for x in x_range) + ' ║')
    print('╚' + '═' * (2*len(x_range) + 1) + '╝')
```

and test our code:

```python3
# Settings:
x_range = range(-3,10)
y_range = range(-3,15)
pattern = ("..OOO..",   ##########################
           "..O.O..",   #                        #
           "..O.O..",   #    RIP John Conway     #
           "...O...",   #      (1937-2020)       #
           "O.OOO..",   #                        #
           ".O.O.O.",   # https://xkcd.com/2293/ #
           "...O..O",   #                        #
           "..O.O..",   ##########################
           "..O.O..")

# Main loop:
universe = read_GameOfLife(pattern)
while(True):
    show_GameOfLife(universe, x_range, y_range)
    universe = next_GameOfLife(universe)
    wait     = input("\nPress <Return> to perform a step.")
    print("\x1b[1A\x1b[2K\x1b[1A\x1b[2K\x1b[1A")
```

## Summary

 * **Try to achieve elegance.** Even for a seemingly simple task like this one, there always will be several approaches you can use. If the code is getting ugly, you should reconsider your initial assumptions.
 * **Efficiency via elegance.** In a high-level language like Python, elegant code is, very often, efficient code. Python's default data structures are faster that whatever you might be able to implement on your own (and will become more efficient in the future without your intervention). You should know which coding patterns are more efficient in your language of choice.
 * **Flexibility via elegance.** A 15 lines-of-code implementation is something you can read, understand and rewrite in 10 minutes. Very often, trying to achieve a flexible implementation results in an overly complex code that nobody is able to modify/adapt/upgrade.
 * **Elegance is hard to achieve.** No one is able to do it right at first. It took me many years to interiorize the lessons I explained in this tutorial. Keep learning and keep sharing your knowledge, so others can learn too.
