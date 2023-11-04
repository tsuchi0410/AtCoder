N = int(input())
M = 1010
imos = [[0] * (M + 1) for _ in range(M + 1)]
for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    imos[ry][lx] -= 1
    imos[ly][rx] -= 1
    imos[ry][rx] += 1
    imos[ly][lx] += 1

# 横方向
for i in range(M + 1):
    for j in range(1, M + 1):
        imos[i][j] += imos[i][j - 1]

# 縦方向
for i in range(1, M + 1):
    for j in range(M + 1):
        imos[i][j] += imos[i - 1][j]

d = {}
for i in range(N + 1):
    d[i] = 0

for i in range(M + 1):
    for j in range(M + 1):
        d[imos[i][j]] += 1

del d[0]
for k, v in d.items():
    print(v)