a,b,x=(int(x) for x in input().split())

def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    d = len(str(arg))    
    return a*arg+b*d <= x

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans=meguru_bisect(10**9+1, 0)
print(ans)