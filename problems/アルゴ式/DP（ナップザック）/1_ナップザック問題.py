n, w = (int(x) for x in input().split())
wv = []
for i in range(n):
    a, b = (int(x) for x in input().split())
    wv.append([a, b])
    
dp = [[0] * (w+1) for _ in range(n)]

for i in range(n):
    for j in range(w+1):

        # 初期値
        if j == wv[i][0]:
            dp[i][j] = max(dp[i][j], wv[i][1])
            
        if i == n-1:
            break

        # under
        if dp[i][j] > 0:
            dp[i+1][j] = max(dp[i][j], dp[i+1][j])
        
        # next
        if dp[i][j] > 0 and j + wv[i+1][0] <= w:
            dp[i+1][j + wv[i+1][0]] = max(dp[i+1][j + wv[i+1][0]], dp[i][j] + wv[i+1][1])

print(max(dp[-1]))