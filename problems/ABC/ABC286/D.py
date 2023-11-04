n,x = (int(x) for x in input().split())
inf = 2501
dp = [[False] * (x+1) for _ in range(inf)]
l = []
for i in range(n):
    a,b = (int(x) for x in input().split())
    for j in range(b):
        l.append(a)

for i in range(len(l)):
    for j in range(x+1):
        
        # new
        if j == l[i]:
            dp[i][j] = True
            
        # end
        if i == len(l) - 1:
            continue

        # next
        if dp[i][j] == True:
            # under
            dp[i+1][j] = dp[i][j]
            
            if j + l[i+1] < x+1:
                dp[i+1][j+l[i+1]] = True

for i in range(len(dp)):
    if dp[i][x] == True:
        print("Yes")
        exit()
print("No")