################################################################################

"""A minimalist implementation of the Game of Life cellular automaton."""

__author__   = "Carlos Luna-Mota"
__license__  = "The Unlicense"
__version__  = "20210327"
__all__      = ["next_GameOfLife", "read_GameOfLife", "show_GameOfLife"]

################################################################################

from collections import defaultdict

def next_GameOfLife(universe):
    """Performs a single iteration of Game of Life in a boundless universe."""

    candidates = defaultdict(int)
    for (x,y) in universe:
        for (dx,dy) in (0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1):
            candidates[x+dx,y+dy] += 1

    new_universe = set()
    for cell,neighbors in candidates.items():
        if neighbors == 3 or (neighbors == 2 and cell in universe):
            new_universe.add(cell)

    return new_universe

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

################################################################################

if __name__ == '__main__':

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
    while True:
        show_GameOfLife(universe, x_range, y_range)
        universe = next_GameOfLife(universe)
        wait     = input("\nPress <Return> to perform a step.")
        print("\x1b[1A\x1b[2K\x1b[1A\x1b[2K\x1b[1A")

################################################################################
