#!/usr/bin/python
# -*- coding: utf-8 -*-

"""A borderless implementation of the Game of Life cellular automaton."""

__author__   = "Carlos Luna-Mota"
__license__  = "The Unlicense"
__version__  = "20200415"
__all__      = ["GameOfLife", "show"]

################################################################################

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

def show(universe, (X,Y)):
    """Prints a rectangular portion of the universe on the screen."""

    length = 2*(X[1]-X[0]) + 1
    print('╔'+ '═'*length + '╗')
    for y in reversed(range(*Y)):
        row = ' '.join('■' if (x,y) in universe else ' ' for x in range(*X))
        print('║ ' + row  + ' ║')
    print('╚' + '═'*length + '╝')

################################################################################

if __name__ == '__main__':

    try: input = raw_input  # Python 2
    except NameError: pass  # Python 3

    # The set of living cells:  https://xkcd.com/2293/
    universe = {(0,4),(1,3),(2,0),(2,1),(2,4),(2,6),(2,7),
                (2,8),(3,2),(3,3),(3,4),(3,5),(3,8),(4,0),
                (4,1),(4,4),(4,6),(4,7),(4,8),(5,3),(6,2)}

    # The visible universe: (x_range, y_range)
    window = ((-3,10), (-3,15))                 

    # Press Ctrl+C to exit:
    while(True):
        show(universe, window)
        universe = GameOfLife(universe)
        stop = input("\nPress <Return> to perform a step.")
        print("\x1b[1A\x1b[2K\x1b[1A\x1b[2K\x1b[1A")
        if stop: break
        
################################################################################
