n = int(input())
t = list(map(int,input().split()))

inf = 100 * (10 ** 3) + 1
dp = [[0] * inf for _ in range(n)]
for i in range(n):
    for j in range(inf):
        
        if i == n-1:
            continue
        
        # 初期値
        if j == t[i]:
            dp[i][j] = 1
        
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        
        if dp[i][j] == 1:
            dp[i+1][j+t[i+1]] = 1

ans = max(t)
d = float('inf')

for i in range(inf):
    if dp[-1][i] == 1:
        if d > abs(i - sum(t) // 2):
            d = abs(i - sum(t) // 2)
            ans = i

print(max(ans, sum(t) - ans))