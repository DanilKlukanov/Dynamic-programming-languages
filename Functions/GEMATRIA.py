word = [str(i) for i in input().split()]
print(*sorted(word, key = lambda x: (sum([ord(p) - ord('A') + 1 for p in x.upper()]), x)), sep = '\n')