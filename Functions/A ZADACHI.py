coll_group=int(input())
dic = {}
for i in range(coll_group):
    num = int(input())
    for j in range(num):
        name, coll = input().split()
        dic[name] = coll

booling = [int(elem[1]) > 1 for elem in dic.items()]

if all(booling) == True:
    print('ДА')
elif all(booling) == False:
    print('НЕТ')