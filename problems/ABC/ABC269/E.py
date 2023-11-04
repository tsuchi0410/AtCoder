n = int(input())
t = int()
n2 = n
a = 0; b = n; c = 0; d = n
while True:
    print('?', str(a), str(a + b // 2), str(c), str(d))
    t = int(input())
    if abs(a - b // 2) == 1:
        if t == 0:
            y = b // 2
        else:
            y = b // 2 + 1
        break
    else:
        if t == n // 2:
            a = b // 2
        else:
            b = b // 2
    n //= 2

n = n2
a = 0; b = n; c = 0; d = n
while True:
    print('?', str(a), str(b), str(c), str(c + (d - c) // 2))
    t = int(input())
    if abs(c - d // 2) == 1:
        if t == 0:
            x = d // 2
        else:
            x = d // 2 + 1
        break
    else:
        if t == n // 2:
            c = d // 2
        else:
            d = d // 2
    n //= 2

print('!', x, y)
