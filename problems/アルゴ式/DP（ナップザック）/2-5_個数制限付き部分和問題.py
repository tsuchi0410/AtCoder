n, m = (int(x) for x in input().split())
a = []; b = []
for i in range(n):
    aa, bb = (int(x) for x in input().split())
    a.append(aa); b.append(bb)

dp = [[False] * (m+1) for _ in range(n)]
for i in range(n):
    cnt = 1
    for j in range(m+1):
        
        
        # 初期値
        if j == a[i] * cnt and b[i] > 0:
            dp[i][j] = True
            cnt += 1; b[i] -= 1
            
        if i == n-1:
            continue

        # under
        if dp[i][j] == True:
            dp[i+1][j] = True
        
            # next
            if j + a[i+1] <= m:
                dp[i+1][j + a[i+1]] = True

if dp[-1][-1] == True:
    print('Yes')
else:
    print('No')

print(dp)