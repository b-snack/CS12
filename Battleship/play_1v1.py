import copy
import time
import battleship_studentname
import gemini_bot

BOARD_SIZE = 10
TOTAL_SHIPS = 5
SHIP_LENGTH = 5
TOTAL_SHIP_CELLS = TOTAL_SHIPS * SHIP_LENGTH
MAX_TURNS = 100

def create_board():
    return [[0] * BOARD_SIZE for i in range(BOARD_SIZE)]

def print_match_state(track1, name1, track2, name2, turn):
    """Prints both 10x10 tracking grids side-by-side in terminal."""
    symbols = {0: ".", 2: "O", 3: "X"}
    
    print("TURN:",turn)
    print(f"{name1:^23} {name2:^23}")
    print(" ", " ".join(str(n) for n in range(BOARD_SIZE))\
          , "|  ", " ".join(str(n) for n in range(BOARD_SIZE)))
    
    for r in range(BOARD_SIZE):
        row1 = " ".join(symbols[track1[r][c]] for c in range(BOARD_SIZE))
        row2 = " ".join(symbols[track2[r][c]] for c in range(BOARD_SIZE))
        print(r, row1, "|", r, row2)

def count_remaining(board):
    count = 0
    for i in board:
        for j in i:
            if j == 1:
                count += 1
    return count

def run_1v1(bot1, bot2, enter, display):
    
    # initial board setups
    board1 = bot1.place_ships(create_board())
    board2 = bot2.place_ships(create_board())
    
    # board to track moves
    track1 = create_board()
    track2 = create_board()
    
    # Stores lists of [row, col, hit_boolean]
    moves_history1 = []
    moves_history2 = []
    
    ships1_left = TOTAL_SHIP_CELLS
    ships2_left = TOTAL_SHIP_CELLS
    
    for turn in range(1, MAX_TURNS + 1):
        # Player 1 
        r, c = bot1.make_move(copy.deepcopy(track1), copy.deepcopy(moves_history1))
        is_hit1 = (board2[r][c] == 1 or board2[r][c]== 3)
        moves_history1.append([r, c, is_hit1])
        
        if is_hit1 == True:
            track1[r][c] = 3
            board2[r][c] = 3
        else:
            track1[r][c] = 2
            
        if count_remaining(board2) == 0:
            print_match_state(track1, bot1.BOT_NAME, track2, bot2.BOT_NAME, turn)
            print("WINNER:", bot1.BOT_NAME)
            return

        # Player 2
        r, c = bot2.make_move(copy.deepcopy(track2), copy.deepcopy(moves_history2))
        is_hit2 = (board1[r][c] == 1 or board1[r][c]== 3)
        moves_history2.append([r, c, is_hit2])
        
        if is_hit2:
            track2[r][c] = 3
            board1[r][c] = 3
        else:
            track2[r][c] = 2
            
        if count_remaining(board1) == 0:
            print_match_state(track1, bot1.BOT_NAME, track2, bot2.BOT_NAME, turn)
            print("WINNER:", bot2.BOT_NAME)
            return
        if display == True:
            print_match_state(track1, bot1.BOT_NAME, track2, bot2.BOT_NAME, turn)
        if enter == True:
            input()

    print("MATCH DRAWN")

if __name__ == "__main__":
    run_1v1(battleship_studentname, gemini_bot, enter = False, display = False)