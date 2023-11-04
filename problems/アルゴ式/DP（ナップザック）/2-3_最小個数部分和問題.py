n, m = (int(x) for x in input().split())
a = list(map(int,input().split()))
inf = float('inf')
dp = [[inf] * (m+1) for _ in range(n)]
for i in range(n):
    for j in range(m+1):
        
        # 初期値
        if j == a[i]:
            dp[i][j] = 1
            
        if i == n-1:
            continue

        # under
        if dp[i][j] > 0 and dp[i][j] != inf:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        
            # next
            if j + a[i+1] <= m:
                dp[i+1][j + a[i+1]] = min(dp[i+1][j + a[i+1]], dp[i][j] + 1)

if dp[-1][-1] == inf:
    print('-1')
else:
    print(dp[-1][-1])