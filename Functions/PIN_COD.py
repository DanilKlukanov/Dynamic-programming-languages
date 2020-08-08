def check_pin(pin):
    n = int(pin[1][::-1])
    m = int(pin[0])
    if is_prime(m) == True and int(pin[1]) == n and int(pin[2]) & (int(pin[2]) - 1) == 0:
        return 'Корректен'
    else:
        return 'Некорректен'

def is_prime(m):
    if m % 2 == 0:
        return m == 2
    d = 3
    while d * d <= m and m % d != 0:
        d += 2
    return d * d > m

pin = [str(i) for i in input().split('-')]
print(check_pin(pin))