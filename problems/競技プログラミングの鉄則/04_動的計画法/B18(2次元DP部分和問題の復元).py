N, S = map(int, input().split())
A = list(map(int,input().split()))

dp = [[0] * (S + 1) for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = True

for i in range(1, N + 1):
    for j in range(S + 1):
        
        # set
        if A[i - 1] == j:
            dp[i][j] = True
        
        # check
        if i == N:
            continue

        if dp[i][j] == True:
            # under
            dp[i + 1][j] = True
            # next
            if j + A[i] < S + 1:
                dp[i + 1][j + A[i]] = True

# for i in dp:
#     print(i)
    
if dp[-1][-1] != True:
    print(-1)
else:
    L = []
    v = N
    cnt = S
    while cnt != 0:
        if cnt - A[v - 1] >= 0 and dp[v - 1][cnt - A[v - 1]] == True:
            cnt -= A[v - 1]
            L.append(v)
        v -= 1


    L.reverse()
    print(len(L))
    print(*L)