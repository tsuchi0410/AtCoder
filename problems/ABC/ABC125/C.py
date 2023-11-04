import math
N = int(input())
A = list(map(int,input().split()))

if N == 2:
    print(max(A[0], A[1]))
    exit()

r = [A[0]]
for i in range(1, N):
    r.append(math.gcd(r[i - 1], A[i]))
l = [A[-1]]
cnt = 0
for i in range(N - 2, -1, -1):
    l.append(math.gcd(l[cnt], A[i]))
    cnt += 1
r.reverse()
ans = 0
for i in range(N):
    if i == 0:
        ans = max(ans, r[1])
    elif i == N - 1:
        ans = max(ans, l[-2])
    else:
        ans = max(ans, math.gcd(l[i - 1], r[i + 1]))

print(ans)