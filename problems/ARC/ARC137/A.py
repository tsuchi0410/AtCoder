import math
L, R = map(int, input().split())
for i in range(R - L, -1, -1):
    for j in range(L, R + 1):
        if j + i > R:
            break
        if math.gcd(j, j + i) == 1:
            print(i)
            exit()