N = int(input())
A = list(map(int,input().split()))

ans = 0
f = 0

while f == 0:
    for i in range(N):
        if (A[i] % 2) == 0:
            A[i] = A[i] / 2
        else:
            f = 1
    
    if f == 0:
        ans += 1

print(ans)

