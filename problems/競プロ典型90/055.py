N, P, Q = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N):
    A[i] %= P
cnt = 0
for i in range(N):
    num = A[i]
    for j in range(i+1, N):
        num2 = (num * A[j]) % P
        for k in range(j+1, N):
            num3 = (num2 * A[k]) % P
            for l in range(k+1, N):
                num4 = (num3 * A[l]) % P
                for m in range(l+1, N):
                    num5 = (num4 * A[m]) % P
                    if num5 == Q:
                        cnt += 1
                    
print(cnt)