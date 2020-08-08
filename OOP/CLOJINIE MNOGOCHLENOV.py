class Polynomial:

    def __init__(self, lis):
        self.list = lis.copy()
        self.size = len(lis)
    
    def __call__(self, others):
        resul = 0
        for i in range(self.size):
            resul = resul + self.list[i] * (others**i)
        return resul
    
    def __add__(self, others):
        maxi = max(len(self.list), len(others.list))
        polynom_new = [0 for i in range(maxi)]
        for i in range(maxi):
            if self.size > i:
                polynom_new[i] = polynom_new[i] + self.list[i]
            if len(others.list) > i:
                polynom_new[i] = polynom_new[i] + others.list[i]
        return Polynomial(polynom_new)  
a = [0, 1]

poly1 = Polynomial(a)
poly2 = Polynomial([10, 11, 12])
poly3 = poly1 + poly2
poly4 = poly2 + poly1
print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))
print(a)