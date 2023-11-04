def is_ok(mid):
    # 美味しさが mid 以上のとき、個数が K 個以上か？
    cnt = 0
    for i in range(X):
        x = mid - A[i]
        idx = bisect.bisect_left(BC, x)
        cnt += len(BC) - idx
    if cnt >= K:
        return False
    else:
        return True 

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    # for _ in range(10**4):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ng

import bisect

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

BC = []
for i in range(Y):
    for j in range(Z):
        BC.append(B[i] + C[j])
BC.sort()
deli_min = meguru_bisect(0, 10 ** 18)

ans = []
for i in range(X):
    x = deli_min - A[i]
    idx = bisect.bisect_left(BC, x)
    if idx != len(BC):
        for j in range(len(BC) - 1, idx - 1, -1):
            ans.append(A[i] + BC[j])

ans.sort(reverse=True)
for i in range(K):
    print(ans[i])