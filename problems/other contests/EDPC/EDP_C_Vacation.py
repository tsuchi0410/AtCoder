n = int(input())
abc = []
dp = []
for i in range(n):
    a, b, c = (int(x) for x in input().split())
    dp.append([0, 0, 0])
    abc.append([a, b, c])
    
dp[0][0] = abc[0][0]
dp[0][1] = abc[0][1]
dp[0][2] = abc[0][2]

for i in range(n-1):
    for j in range(3):
        
        if j == 0:
            dp[i+1][j] = max(dp[i][1] + abc[i+1][j], dp[i][2] + abc[i+1][j])
        elif j == 1:
            dp[i+1][j] = max(dp[i][0] + abc[i+1][j], dp[i][2] + abc[i+1][j])
        else:
            dp[i+1][j] = max(dp[i][0] + abc[i+1][j], dp[i][1] + abc[i+1][j])

# print(dp)
print(max(dp[-1]))