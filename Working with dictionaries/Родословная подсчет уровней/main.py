fin = open('input.txt', 'r')
fout = open('output.txt', 'w')

n = int(fin.readline())

kind, people = {}, {}
kin = []

for i in range(0, n-1):
    kid, parent = fin.readline().split()
    kind[kid] = parent
    kin.append(kid)
    kin.append(parent)

kin = set(kin)

for i in kin:
    count = 0
    chel = i
    while kind.get(chel, 0) != 0:
        chel = kind.get(chel, 0)
        count += 1
    people[i] = count

kin = sorted(list(kin))

for i in kin:
    fout.write(str(i) + " " + str(people.get(i)) + '\n')