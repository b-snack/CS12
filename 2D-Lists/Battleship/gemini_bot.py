"""
Battleship Test Bot
Algorithm: Checkerboard Parity Hunt + 4-Directional Priority Targeting Queue
"""

import random

BOT_NAME = "Gemmy"

GRID_SIZE = 10
TOTAL_SHIPS = 5
SHIP_LENGTH = 5


def place_ships(grid):
    """
    Places 5 ships of length 5 spread out across the perimeter and interior
    with minimal clustering to avoid giving away free adjacent hits.
    """
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            grid[r][c] = 0

    # Ship 1: Horizontal along top perimeter
    for c in range(0, 5):
        grid[0][c] = 1

    # Ship 2: Horizontal along bottom perimeter
    for c in range(5, 10):
        grid[9][c] = 1

    # Ship 3: Vertical along right edge
    for r in range(1, 6):
        grid[r][9] = 1

    # Ship 4: Vertical mid-left
    for r in range(3, 8):
        grid[r][2] = 1

    # Ship 5: Horizontal interior
    for c in range(4, 9):
        grid[5][c] = 1

    return grid


def make_move(opp_grid, prev_moves):
    """
    Decides the next move based on a target queue if hits exist,
    otherwise fires using checkerboard parity hunt mode.
    """
    rows = len(opp_grid)
    cols = len(opp_grid[0])

    # 1. SCAN FOR ACTIVE HITS TO BUILD TARGET QUEUE
    # Collect all unshot orthogonal neighbors around existing hits
    target_candidates = set()
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if opp_grid[r][c] == 3:  # Known hit
                for dr, dc in offsets:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if opp_grid[nr][nc] == 0:  # Valid unshot tile
                            target_candidates.add((nr, nc))

    # If targets exist, pick one (prioritize neighbors of the most recent hit)
    if target_candidates:
        if prev_moves:
            for r, c, is_hit in reversed(prev_moves):
                if is_hit:
                    # Pick an unshot neighbor of the freshest hit first
                    for dr, dc in offsets:
                        candidate = (r + dr, c + dc)
                        if candidate in target_candidates:
                            return candidate

        # Fallback to any active target neighbor
        return target_candidates.pop()

    # 2. PARITY HUNT PHASE (Checkerboard scan)
    # Target only cells where (r + c) is even to find ships faster
    parity_moves = []
    for r in range(rows):
        for c in range(cols):
            if opp_grid[r][c] == 0 and (r + c) % 2 == 0:
                parity_moves.append((r, c))

    if parity_moves:
        return random.choice(parity_moves)

    # 3. CLEANUP PHASE
    # If all parity squares are exhausted, sweep any remaining unknown square
    remaining = [
        (r, c)
        for r in range(rows)
        for c in range(cols)
        if opp_grid[r][c] == 0
    ]

    return random.choice(remaining)