n = int(input())
towns = {}

for i in range(n):
    country, *cities = input().split()
    for i in cities:
        towns[i] = country

m = int(input())
a = []

for i in range(m):
    newtowns = input()
    a.append(towns[newtowns])
for i in range(len(a)): print(a[i])