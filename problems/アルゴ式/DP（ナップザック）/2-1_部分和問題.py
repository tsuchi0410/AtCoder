n, m = (int(x) for x in input().split())
a = list(map(int,input().split()))

dp = [[False] * (m+1) for _ in range(n)]
for i in range(n):
    for j in range(m+1):
        
        # 初期値
        if j == a[i]:
            dp[i][j] = True
            
        if i == n-1:
            continue

        # under
        if dp[i][j] == True:
            dp[i+1][j] = True
        
        # next
        if dp[i][j] == True and j + a[i+1] <= m:
            dp[i+1][j + a[i+1]] = True

if dp[-1][-1] == True:
    print('Yes')
else:
    print('No')