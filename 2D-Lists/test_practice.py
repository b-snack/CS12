def check_matrix(grid):
  is_matrix = True
  for i in range(len(grid)):
    if len(grid[i]) == len(grid[0]):
      is_matrix = True
    else:
      is_matrix = False
      return is_matrix

  return is_matrix


def check_square_matrix(grid):
  is_matrix = True
  for i in range(len(grid)):
    if len(grid[i]) == len(grid):
      is_matrix = True
    else:
      is_matrix = False
      return is_matrix

  return is_matrix


def coordinates(coordinates):
  max_row = 0
  max_column = 0
  for i in coordinates:
    if i[0] >= max_row:
      max_row = i[0]
    if i[1] >= max_column:
      max_column = i[1]

  grid = []
  for i in range(max_row+1):
    sublist = []
    for _ in range(max_column+1):
      sublist.append(0)
    grid.append(sublist)

  for i in coordinates:
    grid[i[0]][i[1]] = 1

  return grid


def minesweeper(grid, row, column):
  offsets = [
    (-1, -1), #Northwest
    (1, -1), #Northeast
    (0, -1), #North
    (-1, 0), #West
    (1, 0), #East
    (-1, 1), #Southwest
    (0, 1), #South
    (1, 1) #Southeast
  ]

  if grid[row][column] == 1:
    return -1
  else:
    total = 0
    for _ in range(len(offsets)):
        r = row+offsets[_][0]
        c = column+offsets[_][1]
        if r >= 0 and c >= 0:
          try:
            total += grid[r][c]
          except IndexError:
            pass

    return total

print(minesweeper([[0, 0, 0, 1], [0, 1, 0, 0], [0, 1, 1, 1], [1, 0, 0, 0]], 3, 1))