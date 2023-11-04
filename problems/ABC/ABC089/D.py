H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
dic = {}
for i in range(H):
    for j in range(W):
        dic[A[i][j]] = [i, j]

S = {}
for i in range(1, H * W + 1):
    num = i % D
    if not num in S:
        S[num] = [0]
    else:
        S.append(dic)
