n, m = input().split()
a = []
for i in range(int(n)):
    a.append([int(j) for j in input().split()])
h = []
for i in range (int(m)):
    for j in range(int(n)):
        h.append(a[j][i])
print(h)
p =[h[i:i+int(n)] for i in range(0, len(h), int(n))]
print(p)
for row in p:
    print(' '.join([str(elem) for elem in row]))