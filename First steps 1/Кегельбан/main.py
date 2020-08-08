n, k = input().split()
line = []  
for i in range(int(n)):
    line.append('I')
for f in range(int(k)):
     s, d = input().split()
     for f in range(int(s)-1, int(d)):
        line[f] = '.'
print(''.join(line))