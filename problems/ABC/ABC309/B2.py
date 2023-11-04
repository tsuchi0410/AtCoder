from collections import deque

N = int(input())
S = [list(input()) for _ in range(N)]

q = deque([])
for i in range(N):
    q.append(S[0][i])
for i in range(1, N):
    q.append(S[i][N - 1])
for i in range(N - 2, -1, -1):
    q.append(S[N - 1][i])
for i in range(N - 2, 0, -1):
    q.append(S[i][0])

q.rotate()
for i in range(N):
    S[0][i] = q.popleft()
for i in range(1, N):
    S[i][N - 1] = q.popleft()
for i in range(N - 2, -1, -1):
    S[N - 1][i] = q.popleft()
for i in range(N - 2, 0, -1):
    S[i][0] = q.popleft()

for i in S:
    print("".join(i))