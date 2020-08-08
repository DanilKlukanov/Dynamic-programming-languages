class Base_oblect:
    x : int
    y : int
    z : int 

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def get_coordinates(self):
        return [self.x, self.y, self.z]

class Block(Base_oblect):
    def shatter(self):
        self.x = None
        self.y = None
        self.z = None

class Entity(Base_oblect):
    def move(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Thing(Base_oblect):
    pass