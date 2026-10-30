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

def n_by_n(x, y):
  grid = []
  sublist = []

  for i in range(y):
    if i % 2 == 0:
      for _ in range(x):
        if _ % 2 == 0:
          sublist.append(0)
        else:
          sublist.append(1)
    elif i % 2 == 1:
      for _ in range(x):
        if _ % 2 == 0:
          sublist.append(1)
        else:
          sublist.append(0)
    grid.append(sublist[:])
    sublist = []

  return grid

def symmetrical_square_matrix(grid):
  for row in range(len(grid)):
    for column in range(len(grid[0])):
      if grid[row][column] != grid[column][row]:
        return False

  return True

def magical_square(grid):
  sums = []
  for row in range(len(grid)):
    total = 0
    for item in range(len(grid[0])):
      total += grid[row][item]
    sums.append(total)

  for column in range(len(grid[0])):
    total = 0
    for item in range(len(grid)):
      total += grid[item][column]
    sums.append(total)

  diag_total = 0
  for diagonal in range(len(grid)):
    diag_total += grid[diagonal][diagonal]
  sums.append(diag_total)

  inv_diag_total = 0
  for diagonal in range(len(grid)):
      inv_diag_total += grid[diagonal][len(grid) - 1 - diagonal]
  sums.append(inv_diag_total)

  magical = True
  for i in range(len(sums)):
    if i == len(sums) - 1:
      if sums[i] != sums[0]:
        magical = False
    elif sums[i] != sums[i+1]:
        magical = False

  return magical

def rotate_matrix(grid):
  rotated = []
  columns = len(grid[0])
  rows = len(grid)

  for column in range(columns):
    sublist = []
    for row in range(rows):
      sublist.append(grid[row][column])
    rotated.append(sublist)

  return rotated


grid_1_test = [
  [1, 2, 3, 4], 
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]

print(rotate_matrix(grid_1_test))

def remove(m, p, q):
  new_matrix = []
  rows = len(m)
  columns = len(m[0])
  for row in range(rows):
    sublist = []
    if row != p:
      for col in range(columns):
        if col != q:
          sublist.append(m[row][col])
      new_matrix.append(sublist)

  return new_matrix


def f(m):
  if len(m) == 1:
    return m[0][0]

  else:
    total = 0
    for q in range(len(m[0])):
      total += m[0][q] * f(remove(m, 0, q))

    return total

m = [
  [3, 8, 2],
  [1, 6, 9],
  [7, 5, 4]
print(remove(m, 1, 2))
print(f(m))