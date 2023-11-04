def dfs(n, x):
    



N, X = map(int, input().split())
L = [0] * 51
P = [0] * 51
L[0] = 1
P[0] = 1
for i in range(1, 51):
    L[i] = 2 * L[i - 1] + 3
    P[i] = 2 * P[i - 1] + 1

print(dfs(N, X))