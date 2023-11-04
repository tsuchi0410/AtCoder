N,K = (int(x) for x in input().split())
C = list(map(int,input().split()))

ans = 0
cnt = 0
d = {}
for i in range(N):

    if i == 0:
        for j in range(K):
            if C[j] in d:
                d[C[j]] += 1
            else:
                d[C[j]] = 1
                cnt += 1
    
    if i > 0:
        if C[i+K-1] in d:
            d[C[i+K-1]] += 1
        else:
            d[C[i+K-1]] = 1
            cnt += 1
        
        if d[C[i-1]] >= 2:
            d[C[i-1]] -= 1
        else:
            del d[C[i-1]]
            cnt -= 1
    
    ans = max(ans, cnt)

    if i+K-1 == N-1:
        print(ans)
        exit()

