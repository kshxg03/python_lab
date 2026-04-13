import math

class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate


    def dist_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)


    def __str__(self):
        return f"P({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __lt__(self, other):
        return self.dist_from_origin() < other.dist_from_origin()

    def __gt__(self, other):
        return self.dist_from_origin() > other.dist_from_origin()

    def __le__(self, other):
        return self.dist_from_origin() <= other.dist_from_origin()

    def __ge__(self, other):
        return self.dist_from_origin() >= other.dist_from_origin()

    def __eq__(self, other):
        return self.dist_from_origin() == other.dist_from_origin()

    def __ne__(self, other):
        return self.dist_from_origin() != other.dist_from_origin()


p_1 = Point(3, 4)
p_2 = Point(1, 2)


print(p_1)  
print(p_2)  


p_3 = p_1 + p_2
print("p_3:", p_3)


print("Distance p_1:", p_1.dist_from_origin())
print("Distance p_2:", p_2.dist_from_origin())


print("p_1 > p_2:", p_1 > p_2)
print("p_1 < p_2:", p_1 < p_2)
print("p_1 >= p_2:", p_1 >= p_2)
print("p_1 <= p_2:", p_1 <= p_2)
print("p_1 == p_2:", p_1 == p_2)
print("p_1 != p_2:", p_1 != p_2)