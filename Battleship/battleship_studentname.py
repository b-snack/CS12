"""
Battleship Game
ICS4U 
Sebastian Wu
This is a virtual version of battleship, written in python to show understanding of 2D Lists. 

Version 1: Initial brainstorming + Strategy Research; placed all ships and found out about probability density methods
Version 2: After place_ships function was completed, I settled on using th eprobability density in order to determine which squares to
           "hunt". This meant that I'd go through windows of five in all cardinal directions and add 1 for squares that could potentially hold
           an opponent's battleship. This meant learning a bit more about for loops like how to iterate through set windows in 2D lists. 

Version 3: Worked on "hunt" function, which is the probability mapping. This adds 1 for each slice of 5 and iterates through, adding 1 to each potential 
           location, and ignores / doesn't add to those with adjacent squares that are misses (currently -1; will have to change later)
           Implementing the diagonals were a little tough, but I figured it out after looking it up online. I also had to find a good way to verify if
           there was a number in the given square. I found the solution to be the function "isinstance(val, form)"


Version 4: Worked on "target function". If there has been a hit square, this function takes the adjacent squares and adds a high number 
           like 1000 so that it overshadows all other squares, placing immediate priority on them. However, it still ignores values
           that are -1, or "H" as to not run into repeated errors. Due to there being 8 directions that the next hit could potential be in, 
           I realized that this code could take many more tries to hit the ship than a traditional grid where one may place ships vertically
           or horizontally. Though, this is also potentially overriden by the number of squares the ship cover (25), which is significantly
           more board space occupied. This function took some new logic and was slightly more difficult to implement. 

Version 5: 
"""

import random

BOT_NAME = "YOURBOTNAME"

GRID_SIZE = 10
TOTAL_SHIPS = 5
SHIP_LENGTH = 5
TOTAL_SHIP_CELLS = TOTAL_SHIPS * SHIP_LENGTH
WINDOW_SIZE = 5

def place_ships(grid):
    """"""
    # input grid is all zeroes
    for i in range(10):
        current_row = []
        for _ in range(10):
            current_row.append(0)
        grid.append(current_row)
   
    # place 5 ships of length 5, as 1s by directly modifying grid
    for i in range(2, 7):
        grid[1][i] = 1
   
    for i in range(1, 6):
        grid[i][8] = 1
       
    for i in range(3, 8):
        grid[i][6] = 1
       
    coordinates = [(0, 8), (1, 7), (2, 6), (3, 5), (4, 4)]
    for x, y in coordinates:
        grid[x][y] = 1
       
    coordinates_2 = [(3, 1), (4, 2), (5, 3), (6, 4), (7, 5)]
    for x, y in coordinates_2:
        grid[x][y] = 1
   
    # the grid with all ships placed is the return

    return grid

print(place_ships([]))


def hunt(grid):
    rows = len(grid)
    columns = len(grid[0])

    def apply_plus_one(coords):
        for row, column in coords:
            if grid[row][column] == -1 or grid[row][column] == "H":
                return

        for row, column in coords:
            val = grid[row][column]
            if isinstance(val, (int, float)): # checks if val is in the form of (int or float)
                grid[row][column] += 1

    # --------------- HORIZONTAL --------------------

    for row in range(len(grid)):
        for start in range(len(grid[row]) - WINDOW_SIZE + 1):
            coords = []
            for i in range(WINDOW_SIZE):
                coords.append((row, start + i))
            apply_plus_one(coords)

    # ----------------- VERTICAL ------------------

    for row in range(rows - WINDOW_SIZE + 1):
        for column in range(columns):
            coords = []
            for i in range(WINDOW_SIZE):
                coords.append((row + i, column))
            apply_plus_one(coords)

    # ---------------- DIAGONALS ------------------

    for row in range(rows - WINDOW_SIZE + 1):
        for column in range(columns - WINDOW_SIZE + 1):
            coords = []
            for i in range(WINDOW_SIZE):
                coords.append((row + i, column + i))
            apply_plus_one(coords)

    for row in range(rows - WINDOW_SIZE + 1):
        for column in range(WINDOW_SIZE - 1, columns):
            coords = []
            for i in range(WINDOW_SIZE):
                coords.append((row + i, column - i))
            apply_plus_one(coords)
            
def target(grid):
    rows = len(grid)
    columns = len(grid[0])

    offsets = [
        (-1, 0), # North
        (1, 0), # South
        (0, 1), # East
        (0, -1), # West
        (-1, -1), # Northwest
        (-1, 1), # Northeast
        (1, -1), # Southwest
        (1, 1) # Southeast
    ]

    hit_bonus = 1000

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == "H":
                for changed_row, changed_column in offsets:
                    neighbouring_row, neighbouring_column = row + changed_row, column + changed_column
                    if 0 <= neighbouring_row < rows and 0 <= neighbouring_column < columns:
                        val = grid[neighbouring_row][neighbouring_column]
                        if isinstance(val, (int, float)) and val >= 0:
                            grid[neighbouring_row][neighbouring_column] += hit_bonus


def make_move(opp_grid, prev_moves):
    # Opponent's grid 0:unknown, 2:known miss, 3:known hit
   
    # Your previous moves is a list of [row, column, hit true/false] lists
    # Most recent move is at the end of the list

    rows = len(opp_grid)
    columns = len(opp_grid[0])
    usable_grid = []

    has_active_hit = False


    for row in opp_grid:
        new_row = row[:]
        usable_grid.append(new_row)

    for row in range(rows):
        for column in range(columns):
            cell_value = usable_grid[row][column]
            if cell_value == 3:
                usable_grid[row][column] = "H"
                has_active_hit = True
            elif cell_value == 2:
                usable_grid[row][column] = -1
            else:
                usable_grid[row][column] = 0


    hunt(usable_grid)

    if has_active_hit:
        target(usable_grid)

    best_score = -1
    best_move = None

    for row in range(rows):
        for column in range(columns):
            if opp_grid[row][column] == 0:
                if best_move is None:
                    best_move = (row, column)
                score = usable_grid[row][column]
                if isinstance(score, (int, float)) and score >= best_score:
                    best_score = score
                    best_move = row, column

    return best_move