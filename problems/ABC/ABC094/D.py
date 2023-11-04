n = int(input())
a = list(map(int,input().split()))
N = max(a)
R = 10**10
for i in range(n):
    if a[i] == N:
        continue
    r = a[i]
    if r < N // 2:
        r = N - r
    R = min(R, r)

if len(a) == 2 and 0 in a:
    print(N, 0)
elif R in a:
    print(N, R)
else:
    print(N, N - R)