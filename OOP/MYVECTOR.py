import math
class MyVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, others):
        return MyVector(self.x + others.x, self.y + others.y)
    
    def __iadd__(self, others):
        self.x += others.x
        self.y += others.y
        return self
    
    def __sub__(self, others):
        return MyVector(self.x - others.x, self.y - others.y)
    
    def __mul__(self, others):
        return MyVector(self.x * others, self.y * others)
    
    def __rmul__(self, others):
        return MyVector(self.x * others, self.y * others)

    def __imul__(self, others):
        self.x *= others
        self.y *= others
        return self
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
   
    def __ne__(self, other):
        return self.x != other.x and self.y != other.y
    
    def __len__(self):
        return math.floor(math.sqrt(self.x ** 2 + self.y ** 2))

    def __str__(self):
        return 'MyVector({}, {})'.format(self.x, self.y)
v1 = MyVector(-2, 5)
v2 = MyVector(3, -4)
v_sum = v1 + v2
print(v_sum)