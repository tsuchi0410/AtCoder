N, M = map(int,input().split())
INF = 10 ** 18
cnt = 0
ans = INF
for a in range(1, INF):
    b = (M + cnt) // a
    if a > b:
        break
    if b <= N and a * b >= M:
        ans = min(ans, a * b)
    cnt += 1
print(ans if ans < INF else -1)