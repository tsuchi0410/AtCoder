def is_ok(y, x, mid):
    A = y
    B = x
    C = y + mid
    D = x + mid
    if C >= H + 1 or D >= W + 1:
        return False
    cnt = S[C][D] - S[C][B] - S[A][D] + S[A][B]
    if cnt == 0:
        return True
    else:
        return False

def meguru_bisect(y, x, ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    # for _ in range(10**4):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(y, x, mid):
            ng = mid
        else:
            ok = mid
    return ng


H, W, N = map(int, input().split())
G = [[0] * W for _ in range(H)]
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = 1

S = [[0] * (W + 1) for i in range(H + 1)]
for i in range(H):
    for j in range(W):
        S[i + 1][j + 1] += S[i + 1][j] + S[i][j + 1] - S[i][j] + G[i][j]

ans = 0
for i in range(H):
    for j in range(W):
        ans += meguru_bisect(i, j, 0, 3010)

print(ans)