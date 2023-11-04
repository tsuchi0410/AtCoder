N, W = (int(x) for x in input().split())
V = (10 ** 3) * N 
w = []
v = []
dp = []

for i in range(N):
    a, b = (int(x) for x in input().split())
    w.append(a)
    v.append(b)
    dp.append([float('inf')] * (V+1))
    
for i in range(N):
    for j in range(V+1):
        
        # new
        if j == v[i]:
            dp[i][j] = min(dp[i][j], w[i])
            
        # end
        if i == N - 1:
            continue
            
        # under
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        
        # next
        if dp[i][j] > 0 and dp[i][j] != float('inf'):
            dp[i+1][j+v[i+1]] = min(dp[i+1][j+v[i+1]], dp[i][j] + w[i+1])
            
for i in range(len(dp[-1])-1, -1, -1):
    if dp[-1][i] > 0 and dp[-1][i] <= W:
        if dp[-1][i] != float('inf'):
            print(i)
            exit()