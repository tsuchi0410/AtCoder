n, s = (int(x) for x in input().split())
a = []
b = []
for i in range(n):
    x, y = list(map(int,input().split()))
    a.append(x)
    b.append(y)
    
dp = [[0] * (s+1) for _ in range(n+1)]

dp[0][0] = float('inf')
    
for i in range(n):
    for j in range(s+1):
        
        if i == n-1:
            continue
        
        if dp[i][j] > 0 and j+a[i+1] < s+1:
            dp[i+1][j+a[i+1]] = 1
        if dp[i][j] > 0 and j+b[i+1] < s+1:
            dp[i+1][j+b[i+1]] = 1
            

if dp[-1][-1] == 0:
    print('No')
else:
    ans = []
    for i in range(n-1, -1, -1):
        if dp[i-1][s-a[i]] == 1:
            ans.append('H')
            s -= a[i]
        else:
            ans.append('T')
            s -= b[i]    
    
    ans.reverse()
    print(*ans, sep='')

for i in range(len(dp)):
    print(dp[i])

print(dp)