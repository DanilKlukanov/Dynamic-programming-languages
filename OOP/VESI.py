class Balance:
    def __init__ (self):
        self.right = 0
        self.left = 0

    def add_right(self, r):
        self.right = self.right + r

    def add_left(self, l):
        self.left = self.left + l

    def result (self):
        if self.right > self.left:
            return 'R'
        elif self.right < self.left:
            return 'L'
        elif self.right == self.left:
            return '='

balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())