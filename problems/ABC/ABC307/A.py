N = int(input())
A = list(map(int, input().split()))
ans = 0
l = []
for i in range(7 * N):
    ans += A[i]
    if i != 0 and (i + 1) % 7 == 0:
        l.append(ans)
        ans = 0
print(*l)