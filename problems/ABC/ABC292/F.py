import math

def is_ok(r):
    # 条件を満たすかどうか？問題ごとに定義
    theta = math.acos(A / r)
    if r * math.cos((math.pi / 6) - theta) <= B and math.degrees(theta) <= 30:
        return True
    else:
        return False
    

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    #while (abs(ok - ng) > 0.0000000001):
    for _ in range(10 ** 5):
        mid = (ok + ng) / 2
        if is_ok(mid):
            ng = mid
        else:
            ok = mid
    return ok

A, B = map(int, input().split())
if A > B:
    A, B = B, A

# A <= B
res = meguru_bisect(A, 1500)
print(res)