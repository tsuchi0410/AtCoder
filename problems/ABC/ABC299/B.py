N,T=map(int,input().split())
C = list(map(int,input().split()))
R = list(map(int,input().split()))

if T in C:
    ans = 0
    p = 0
    for i in range(N):
        if C[i] == T and ans < R[i]:
            ans = max(ans, R[i])
            p = i + 1
else:
    T = C[0]
    ans = 0
    for i in range(N):
        if C[i] == T and ans < R[i]:
            ans = max(ans, R[i])
            p = i + 1

print(p)