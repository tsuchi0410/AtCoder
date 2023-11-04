# 二次元リストを90度回転する
for i in range(N):
    for j in range(N):
        L[j][N-1-i] = A[i][j]


# 二次元リストを90度回転する
A = [list(row) for row in zip(*A[::-1])]