A, M, L, R = map(int, input().split())

d = R - L
L2 = L + A
R2 = R + A
d2 = R2 - L2

if L == R:
    print(0)
    exit()

print(d2 // M + 1)