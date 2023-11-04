N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

d = {}
for i in range(M):
    d[i + 1] = []
for i in range(N):
    d[C[i]].append(i)

init = [0] * (M + 1)
for k, v in d.items():
    init[k] = v[-1]


ans = []
L = [0] * (M + 1)
for i in range(N):
    if init[C[i]] != False:
        ans.append(S[init[C[i]]])
        init[C[i]] = False
    else:
        ans.append(S[d[C[i]][L[C[i]]]])
        L[C[i]] += 1

print("".join(ans))