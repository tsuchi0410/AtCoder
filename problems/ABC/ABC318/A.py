N, M, P = map(int, input().split())
ans = 0
for i in range(M, N + 1, P):
    ans += 1
print(ans)