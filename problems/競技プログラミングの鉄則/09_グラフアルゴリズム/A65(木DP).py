N = int(input())
# 2 <= i <= N
A = [0] * 2 + list(map(int,input().split()))
G = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    # 上司 -> 部下の方向に辺を追加
    G[A[i]].append(i)

# dp[x] は社員 x の部下の数
dp = [0] * (N + 1)
for i in range(N, 0, -1):
    for j in G[i]:
        dp[i] += dp[j] + 1

print(*dp[1:])