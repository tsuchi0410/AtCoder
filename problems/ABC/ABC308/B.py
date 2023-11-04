N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))
dic = {}
for i in range(M):
    dic[D[i]] = P[i + 1]

ans = 0
for i in range(N):
    if C[i] in dic:
        ans += dic[C[i]]
    else:
        ans += P[0]
print(ans)