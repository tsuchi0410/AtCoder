q = []
for i in range(N):
    q.append(S[0][i])
for i in range(1, N):
    q.append(S[i][N - 1])
for i in range(N - 2, -1, -1):
    q.append(S[N - 1][i])
for i in range(N - 2, 0, -1):
    q.append(S[i][0])