n, s = (int(x) for x in input().split())
a = []
b = []
for i in range(n):
    x, y = list(map(int,input().split()))
    a.append(x)
    b.append(y)
    
dp = [[-1] * (s+1) for _ in range(n+1)]

dp[0][0] = float('inf')
    
for i in range(n):
    for j in range(s+1):
        
        if dp[i][j] > -1 and j+a[i] < s+1:
            dp[i+1][j+a[i]] = 0
        if dp[i][j] > -1 and j+b[i] < s+1:
            dp[i+1][j+b[i]] = 1
            
        
if dp[-1][-1] == -1:
    print('No')
else:
    ans = []
    for i in range(n, 0, -1):
        if dp[i][s] == 0:
            ans.append('H')
            s -= a[i-1]
        else:
            ans.append('T')
            s -= b[i-1]    
    
    ans.reverse()
    print('Yes')
    print(*ans, sep='')

print(s)
