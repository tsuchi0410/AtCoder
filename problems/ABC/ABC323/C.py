import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

P = [0] * N
for i in range(N):
    P[i] += i + 1

L = [[] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            P[i] += A[j]
        else:
            L[i].append(A[j])

for i in range(N):
    L[i].sort(reverse=True)

S = [[0] for _ in range(N)]
for i in range(N):
    for j in range(len(L[i])):
        S[i].append(S[i][j] + L[i][j])

ans = [0] * N
MAXP = max(P)
for i in range(N):
    nokori = MAXP - P[i]
    idx = bisect.bisect_left(S[i], nokori)
    print(idx)
