n = int(input())


a = [1, 1]
i = 2
if n == 1:
    del a[1]
    print(*a)

elif n == 2:
    print (*a)

if n > 2:
   while i < n:
    a.append (a[i-1] + a[i-2])
    i += 1
   
   print(*a)
   
