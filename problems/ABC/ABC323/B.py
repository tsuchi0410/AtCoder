N = int(input())
S = [input() for _ in range(N)]

dic = {}
for i in range(N):
    dic[i] = 0

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        
        if S[i][j] == "o":
            dic[i] += 1

ans = [0] * N
for k, v in dic.items():
    ans[k] = [v, k + 1]

ans.sort(reverse=True)


L = []
buf = []
for i in range(N - 1):
    if ans[i][0] == ans[i + 1][0]:
        buf.append(ans[i][1])
        if i == N - 2:
            buf.append(ans[-1][1])
    else:
        buf.append(ans[i][1])
        buf.sort()
        L.append(buf)
        buf = []

if len(buf) == 0:
    L.append([ans[-1][1]])
else:
    buf.sort()
    L.append(buf)

for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end = " ")
print()