from collections import deque

def ed(xa, ya, xb, yb):
    return ((xa - xb) ** 2 + (ya - yb) ** 2)

N = int(input())
sx, sy, tx, ty = map(int, input().split())
X = []
Y = []
R = []
for i in range(N):
    x, y, r = map(int, input().split())
    X.append(x)
    Y.append(y)
    R.append(r)


for i in range(N):
    if ed(X[i], Y[i], sx, sy) == R[i] ** 2:
        sv = i
    if ed(X[i], Y[i], tx, ty) == R[i] ** 2:
        gv = i

q = deque([sv])
depth = [False] * N # 頂点数
depth[sv] = True
while q:
    v = q.popleft()
    for nv in range(N):
        if v == nv:
            continue
        if depth[nv] == False:
            if abs(R[v] - R[nv]) ** 2 <= ed(X[v], Y[v], X[nv], Y[nv]) <= (R[v] + R[nv]) ** 2:
                depth[nv] = True
                q.append(nv)

print("Yes") if depth[gv] == True else print("No")