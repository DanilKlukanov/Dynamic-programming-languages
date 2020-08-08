a = [int(i) for i in range(100) if int(i) % 9 == 0]
print(a)
b = list(filter(lambda num: num >= 18, a))
print(sum(map(lambda sq: sq ** 2, b)))