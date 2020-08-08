n = int(input())
dic = {}

for i in range(n):
    word, *trans = input().replace(',','').split()
    del trans[0]
    for j in trans:
        if j not in dic.keys():
            dic[j] = []
        dic[j].append(word)

print(len(dic))

sorttuple = sorted(dic.items())

for i, j in sorttuple:
    print(i, '-', str(j).replace('[', '').replace(']', '').replace('\'', ''))
