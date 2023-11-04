def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    cnt = 0
    pre = 0
    for i in range(n):
        if a[i] - pre >= arg:
            pre = a[i]
            cnt += 1

    # Last
    if l - pre < arg:
        cnt -= 1

    if cnt >= k:
        flag = True
    else:
        flag = False

    return flag

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid) == False:
            ok = mid
        else:
            ng = mid
    return ng

n, l = map(int, input().split())
k = int(input())
a = list(map(int,input().split()))

res = meguru_bisect(0, l+1)
print(res)