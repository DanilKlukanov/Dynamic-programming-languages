n = int(input())
i = [int(i) for i in input().split()]
a = int(input())
print (*(i[(-1*(a%n)):n] + i[:(-1*(a%n))]))  