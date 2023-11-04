import bisect
N = int(input())

T = []
X = []
A = []
maxT = -1
for i in range(N):
    t,x,a = (int(x) for x in input().split())
    T.append(t)
    X.append(x)
    A.append(a)
    maxT = max(maxT, t)
    
dp = []
for i in range(maxT+1):
    dp.append([0]*5)
    

dp[0][0] = True

for i in range(0, maxT):
    for j in range(5):
        
        if dp[i][j] == 0:
            continue
        
        # under
        dp[i+1][j] = max(dp[i][j],dp[i+1][j])
        
        # right
        if j+1 <= 4:
            dp[i+1][j+1] = max(dp[i][j],dp[i+1][j+1])
        
        # left
        if j-1 >= 0:
            dp[i+1][j-1] = max(dp[i][j],dp[i+1][j-1])
            
    # ans
    time = bisect.bisect_left(T, i+1)
    if i+1 == T[time]:
        if dp[i+1][X[time]] > 0:
            dp[i+1][X[time]] += A[time]
            
                                
print(max(dp[-1])-1)