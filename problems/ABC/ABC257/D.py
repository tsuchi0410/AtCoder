from collections import deque

def is_ok(mid):
    # mid = S
    for s in range(N):
        q = deque([s])
        depth = [False] * N # 頂点数
        depth[s] = True
        while q:
            v = q.popleft()
            for nv in range(N):
                if v == nv:
                    continue
                if depth[nv] == False:
                    if P[v] * mid >= abs(X[v] - X[nv]) + abs(Y[v] - Y[nv]):
                        depth[nv] = True
                        q.append(nv)
        
        f = True
        for fv in depth:
            if fv == False:
                f = False
        
        if f == True:
            return True
    
    return False


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
    return ok

N = int(input())
X = []
Y = []
P = []
for i in range(N):
    x, y, p = map(int, input().split())
    X.append(x)
    Y.append(y)
    P.append(p)

S = meguru_bisect(0, 10**18)
print(S)