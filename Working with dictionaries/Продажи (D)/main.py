def count(dic):
    stat = {}

    for f in dic:
        if f[0] in stat:
            num = stat.get(f[0])
            stat[f[0]] = int(num) + int(f[1])
        else:
            stat[f[0]] = f[1]
    
    return sorted(stat.items())

fin = open ('input.txt', 'r')
fout = open('output.txt', 'w')

dic = {}

for i in fin:
    name, thing, pay = i.split()
    if name in dic:
        dic[name].append((thing, pay))
    else:
        dic[name] = [(thing, pay)]
print(dic)
for i in sorted(dic):
    fout.write(i + ':' + '\n')
    for thi, pa in count(dic[i]):
        fout.write(thi + ' ' + str(pa) + '\n')
