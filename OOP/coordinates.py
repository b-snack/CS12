class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def slope(self, other):
        return (self.y-other.y)/(self.x-other.x)
    def __str__(self):
        return ("("+str(self.x)+", "+str(self.y)+")")
A = Point(2, 9)
B = Point(6, 3)
print(A.slope(B))

print(A)

