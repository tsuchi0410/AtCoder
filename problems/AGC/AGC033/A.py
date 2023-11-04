from collections import deque

# 入力
H, W = (int(x) for x in input().split())
A = [input() for _ in range(H)]

# 深さを -1 に初期化
d = [[-1] * W for _ in range(H)]
q = deque([])
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            d[i][j] = 0
            q.append([i, j])

while q:
    y, x = q.popleft()
    for i, j in [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]:
        if i < 0 or j < 0:
            continue
        if i > H - 1 or j > W - 1:
            continue
        if d[i][j] == -1 and A[i][j] == '.':
            q.append([i, j])
            d[i][j] = d[y][x] + 1

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, d[i][j])
print(ans)
