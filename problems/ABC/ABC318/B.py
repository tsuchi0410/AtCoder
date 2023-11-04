N = int(input())

M = 110
imos = [[0] * (M + 1) for _ in range(M + 1)]

for i in range(N):
    A, B, C, D = map(int, input().split())
    ly = C
    lx = A
    ry = D
    rx = B
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

ans = 0
for i in range(M + 1):
    for j in range(M + 1):
        if imos[i][j] >= 1:
            ans += 1
print(ans)