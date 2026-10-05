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
   
    for i in range(0, 6):
        grid[i][8] = 1
       
    for i in range(3, 8):
        grid[i][6] = 1
       
    for i in range(1, 6):
        grid[i][i+2] = 1
   
    coordinates = [(0, 8), (1, 7), (2, 6), (3, 5), (4, 4)]
    for x, y in coordinates:
        grid[x][y] = 1
       
    coordinates_2 = [(3, 1), (4, 2), (5, 3), (6, 4), (7, 5)]
    for x, y in coordinates:
        grid[x][y] = 1
       
   
   
    # the grid with all ships placed is the return
               
    return grid

print(place_ships([]))


def hunt(grid):
    rows = len(grid)
    columns = len(grid[0])

    def apply_plus_one(coords):
        for row, column in coords:
            if grid[row][column] == -1:
                return

        for row, column in coords:
            val = grid[row][column]
            if isinstance(val, (int, float)): # checks if val is in the form of (int, float)
                grid[row][column] += 1

    for row in range(len(grid)):
        for start in range(len(grid[row]) - WINDOW_SIZE + 1):
            coords = []
            for i in range(WINDOW_SIZE):
                coords.append((row, start + i))
            apply_plus_one(coords)

    for row in range(len(rows)):
        for start in range(len(columns) - WINDOW_SIZE + 1):
            coords = []
            for i in range(WINDOW_SIZE):

    row_limit = len(grid) - 5 + 1
    column_limit = len(grid[0]) - 5 + 1

    for row_start in range(row_limit):
        for column_start in range(column_limit):
            for step in range(5):
                grid[row_start + step][column_start + step] += 1



    except:




def make_move(opp_grid, prev_moves):
    # Opponent's grid 0:unknown, 2:known miss, 3:known hit
   
    # Your previous moves is a list of [row, column, hit true/false] lists
    # Most recent move is at the end of the list

    usable_grid = opp_grid[:]


    return (row, col)