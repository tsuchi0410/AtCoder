N = int(input())
A = list(map(int, input().split()))
S = input()

q = "MEX"

dp = []
for i in range(3):
    dp.append([0] * len(S))
 
stM = [set()] * N
stE = [set()] * N
stX = [set()] * N

# 1段目
if q[0] == S[0]:
    dp[0][0] = 1
    stM[0].add(A[0])
 
for j in range(1,len(S)):
    if q[0] == S[j]:
        dp[0][j] = dp[0][j-1] + 1
        stM[j] = {A[j]}
    else:
        dp[0][j] = dp[0][j-1]
        stM[j] = stM[j - 1]
 
# 2段目以降
ans = 0
for i in range(1,3):
    for j in range(len(S)):
        if i - 1 >= j:
            dp[i][j] = 0
            continue
        if q[i] == S[j]:
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            if i == 1:
                if dp[i][j] > 0:
                    stE[j] = stM[j - 1] | {A[j]}
            elif i == 2:
                if dp[i][j] > 0:
                    stX[j] = stE[j - 1] | {A[j]}
                    for k in range(4):
                        if k in stX[j]:
                            continue
                        else:
                            ans += k * dp[i][j]
                            break
        else:
            dp[i][j] = dp[i][j-1]
            if i == 1:
                stE[j] = stE[j - 1]
            elif i == 2:
                stX[j] = stX[j - 1]
 
print(ans)
