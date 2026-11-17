# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def slope(self, other):
#         return (self.y-other.y)/(self.x-other.x)
#     def __str__(self):
#         return ("("+str(self.x)+", "+str(self.y)+")")
# A = Point(2, 9)
# B = Point(6, 3)
# print(A.slope(B))

# print(A)

class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def distance(self, other):
     dist_x = (self.x - other.x) ** 2
     dist_y = (self.y - other.y) ** 2

     total = (dist_x + dist_y) ** (0.5)

     return total

def eqn_of_line(x1, y1, x2, y2):
  slope = (y1 - y2) / (x1 - x2)
  y_shift = y1 - slope * x1

  return f"y = {slope} * x + {y_shift}"

A = Point(2, 9)
B = Point(6, 3)

print(eqn_of_line(A.x, A.y, B.x, B.y))