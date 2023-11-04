"""
長方形区域内の値の総和を高速に求める
"""

N = 4

A = [[1, 7, 0, 6], [5, 8, 1, 11], [10, 4, 2, 201], [3, 16, 0, 1]] # 4*4 リスト
S = [[0] * (N + 1) for i in range(N + 1)] # 累積リストは+1の、5*5リストでの初期化

for i in range(N):
    for j in range(N):
        S[i + 1][j + 1] += S[i + 1][j] + S[i][j + 1] - S[i][j] + A[i][j]

Q = int(input())
for i in range(Q):
    # A, B = 左上, C, D = 右下
    A, B, C, D = map(int, input().split())
    # 調整
    A -= 1
    B -= 1
    ans = S[C][D] - S[C][B] - S[A][D] + S[A][B]
    print(ans)

