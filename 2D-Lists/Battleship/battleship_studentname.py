"""
Battleship Game
ICS4U 
Sebastian Wu
This is a virtual version of battleship, written in python to show understanding of 2D Lists. 
"""

import random

BOT_NAME = "Boom"

GRID_SIZE = 10
TOTAL_SHIPS = 5
SHIP_LENGTH = 5
TOTAL_SHIP_CELLS = TOTAL_SHIPS * SHIP_LENGTH
WINDOW_SIZE = 5

def place_ships(grid):
    """"""
    # input grid is all zeroes
    if not grid:
        for i in range(10):
            grid.append([0] * 10)

    else:
        for row in range(10):
            for column in range(10):
                grid[row][column] = 0
   
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

def calculate_probability(opp_grid):
    rows = len(opp_grid)
    columns = len(opp_grid[0])

    density = []
    for row in range(rows):
        row_sublist = []
        for column in range(columns):
            row_sublist.append(0)
        density.append(row_sublist)

    directions = [
        (1, 0), # South
        (0, 1), # East
        (1, -1), # Southwest
        (1, 1) # Southeast
    ]

    for row in range(rows):
        for column in range(columns):
            for d_row, d_column in directions:

                coords = []
                out_of_bounds = False

                for i in range(WINDOW_SIZE):
                    current_row = row + (i * d_row)
                    current_column = column + (i * d_column)

                    if current_row < 0 or current_row >= rows:
                        out_of_bounds = True
                        break

                    if current_column < 0 or current_column >= columns:
                        out_of_bounds = True
                        break

                    coords.append((current_row, current_column))

                if out_of_bounds: 
                    continue

                has_miss = False
                hits = 0

                for r, c in coords:
                    state = opp_grid[r][c]
                    if state == 2:
                        has_miss = True
                        break

                    elif state == 3:
                        hits += 1

                if has_miss:
                    continue

                if hits == 0:
                    weight = 1
                elif hits == 1:
                    weight = 100
                elif hits == 2:
                    weight = 1000
                elif hits == 3:
                    weight = 10000
                else:
                    weight = 100000

                for r, c in coords:
                    if opp_grid[r][c] == 0:
                        density[r][c] += weight

    return density

def make_move(opp_grid, prev_moves):
    # Opponent's grid 0:unknown, 2:known miss, 3:known hit
   
    # Your previous moves is a list of [row, column, hit true/false] lists
    # Most recent move is at the end of the list

    rows = len(opp_grid)
    columns = len(opp_grid[0])

    density = calculate_probability(opp_grid)

    best_score = -1
    best_coords = []

    for row in range(rows):
        for column in range(columns):
            if opp_grid[row][column] == 0:
                score = density[row][column]
                if score > best_score:
                    best_score = score
                    best_coords = [(row, column)]
                elif score == best_score:
                    best_coords.append((row, column))

    if len(best_coords) > 0:
        return random.choice(best_coords)

    return (0, 0)