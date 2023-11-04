N = int(input())
T = list(map(int, input().split()))

x = 0
for i in range(N):
    x >>= T[i]
    x += 1
    if x % 2 == 0:
        x += 1
    x <<= T[i]
print(x)