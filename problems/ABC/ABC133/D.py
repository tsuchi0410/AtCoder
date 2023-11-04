def is_ok(mid):
    # 条件を満たすかどうか？問題ごとに定義
    num = mid
    for i in range(N):
        next = A[i] - (num // 2)
        num = 2 * next
    
    last = A[-1] - (mid // 2)
    if last == num // 2:
        print("ok")
    else:
        return num

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if mid % 2 == 1:
            mid -= 1
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


N = int(input())
A = list(map(int,input().split()))

meguru_bisect(0, 2 * min(A[-1], A[0]))
