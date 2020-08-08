def list_of_turns(move):
    a = []
    a.append([move[0] + 1, move[1] + 2])
    a.append([move[0] - 1, move[1] + 2])
    a.append([move[0] + 2, move[1] + 1])
    a.append([move[0] + 2, move[1] - 1])
    a.append([move[0] + 1, move[1] - 2])
    a.append([move[0] - 1, move[1] - 2])
    a.append([move[0] - 2, move[1] + 1])
    a.append([move[0] - 2, move[1] - 1])
    return a

move = list(map(int,(input().replace('A', '1').replace('B', '2').replace('C', '3').replace('D', '4').replace('E', '5').replace('F', '6').replace('G', '7').replace('H', '8'))))
fi = list_of_turns(move)
a = []

for i in range(len(fi)):
    if fi[i][0] == -1 or fi[i][1] == -1  or  fi[i][0] == 0 or fi[i][1] == 0  or  fi[i][0] == 10 or fi[i][1] == 10  or  fi[i][0] == 9 or fi[i][1] == 9:
        pass
    else:
        a.append(fi[i])

for i in range(len(a)):
    a[i][0] = str(a[i][0]).replace('1', 'A').replace('2', 'B').replace('3', 'C').replace('4', 'D').replace('5', 'E').replace('6', 'F').replace('7', 'G').replace('8', 'H')
    a[i][1] = str(a[i][1])

b = []
for i in range (len(a)):
    b.append(a[i][0] + a[i][1])
print(sorted(b))