def glubina(n):
  if n==1:
      return [0, 0]
  else:
    return [glubina(n-1), glubina(n-1)]
n = int(input())
print(glubina(n))