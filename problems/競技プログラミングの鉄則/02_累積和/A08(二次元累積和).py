H, W = map(int, input().split())
X = []
for i in range(H):
    x = list(map(int,input().split()))
    X.append(x)

S = [[0] * (W + 1) for i in range(H + 1)]
for i in range(H):
    for j in range(W):
        S[i + 1][j + 1] += S[i + 1][j] + S[i][j + 1] - S[i][j] + X[i][j]

Q = int(input())
for i in range(Q):
    A, B, C, D = map(int, input().split())
    A -= 1
    B -= 1
    ans = S[C][D] - S[C][B] - S[A][D] + S[A][B]
    print(ans)