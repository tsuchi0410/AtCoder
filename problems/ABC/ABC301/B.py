N = int(input())
A = list(map(int,input().split()))

ans = []
for i in range(N-1):
    if A[i] > A[i+1]:
        ans.append(A[i])
        d = A[i] - A[i+1] - 1
        l = []
        for j in range(A[i]-1, A[i+1], -1):
            l.append(j)
        ans += l
    else:
        ans.append(A[i])
        d = A[i+1] - A[i] - 1
        l = []
        for j in range(A[i]+1, A[i+1]):
            l.append(j)
        ans += l
ans.append(A[-1])
print(*ans)