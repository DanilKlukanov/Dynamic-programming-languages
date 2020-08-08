a = int(input())
g = [int(i) for i in input().split()]
f = int(input())
print (len([int(i) for i in g if int(i) >= f] + [f]))