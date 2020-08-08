fin = open("input.txt", "a")

lis = fin.read().split()
dic = {}

for i in lis:
    if i in dic:
        newval = dic.get(i)
        dic[i] = newval + 1
    else:
        dic[i] = 1

newdic = sorted(dic.items(), key = lambda i : -i[1])

count = [[] for i in range(newdic[0][1])]

for i in range(len(newdic)):
    count[-newdic[i][1]].append(newdic[i][0])

for i in count:
    i.sort()
    for p in i:
        print(p)