# Fill in the Line class methods to accept coordinates as a pair of tuples and 
# return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.


class Line:
    def __init__(self, coor1, coor2): 
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
        return distance

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        gradient = ((y2-y1)/(x2-x1))
        return gradient



coordinatel = (3,2)
coordinate2 = (8,10)

line_1 = Line(coordinatel, coordinate2)

print(line_1.distance())  # 9.433981132056603
print(line_1.slope())  # 1.6





# Fill in the class

class Cylinder:
    pia = 3.14
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume (self):
        h = self.height
        r = self.radius
        volume = self.pia * ((r)**2)*h
        return volume

    def surface_area(self):
        h = self.height
        r = self.radius
        A = 2*self.pia*r*(h+r)
        return A

# # EXAMPLE EXECUTION

cylinder = Cylinder(2,3)
print(cylinder.volume())  # 56.52
print(cylinder.surface_area())  # 94.2
