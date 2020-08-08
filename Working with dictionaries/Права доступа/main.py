n = int(input())
alls = {}

for i in range(n):
    fille, *command = input().split()
    alls[fille] = command

m = int(input())
a = []
for i in range(m):
    command1, fille1 = input().split()
    depot = alls.get(fille1)
    if command1 == 'execute': command1 = 'X'
    elif command1 == 'read': command1 = 'R'
    elif command1 == 'write': command1 = 'W'
    if command1 in depot:
        a.append('OK')
    else:
        a.append('Access denied')

for i in range(len(a)): print(a[i])