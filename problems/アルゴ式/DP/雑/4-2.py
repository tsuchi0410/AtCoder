n, k = (int(x) for x in input().split())
a = list(map(int,input().split()))

inf = 10 ** 7 + 1

s = [0]
for i in range(0, n):
    s.append(s[i] + a[i])

dp = [False] * inf
dp[0] = True
cnt = 0
for i in range(inf):
    
    if dp[i] == True:
        if s[cnt+k] - s[cnt] > 0:
            dp[i+(s[i+k] - s[i])] = True
        cnt += 1
        
    if cnt == n:
        break

for i in range(inf-1,-1,-1):
    if dp[i] == True:
        print(i)
        exit()
        