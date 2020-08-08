n, m, k = input().split()
table =[[0 for j in range(int(m)+2)] for i in range(int(n)+2)]
for g in range(int(k)):
    x, y = input().split()
    table[int(x)][int(y)] = '*'
    for i in range(int(x)-1,int(x)+2):
        for j in range(int(y)-1, int(y)+2):
            if table[i][j] != '*':
                table[i][j] = table[i][j] + 1
del table[0]
del table[int(n)]
for v in table:
    print(*(v[1:int(m)+1]))