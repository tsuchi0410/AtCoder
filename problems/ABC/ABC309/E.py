N, M = map(int, input().split())
p = [-1] + list(map(int, input().split()))
dp = [0] * N
for _ in range(M):
    x, y = map(int, input().split())
    dp[x - 1] = max(dp[x - 1], y + 1)

for i in range(1, N):
    dp[i] = max(dp[i], dp[p[i] - 1] - 1)

ans = 0
for i in dp:
    if i >= 1:
        ans += 1
        
print(ans)