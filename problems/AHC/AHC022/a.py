PI = 3.14159
e = 2.71828


L, N, S = map(int, input().split())
for _ in range(N):
    Y, X = map(int, input().split())

P = [[0] * L for _ in range(L)]
pij = 0
for i in range(L):
    for j in range(L):
        if pij == 1001:
            pij = 0
        P[i][j] = pij

G = [[0] * L for _ in range(L)]
for i in range(L):
    for j in range(L):
        res = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu)**2) / (2 * sigma**2))


print(-1, -1, -1)
for i in range(N):
    print(i)