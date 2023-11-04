def is_ok(mid):
    cnt = 0
    for i in range(N):
        if A[i] >= mid:
           cnt += A[i] - mid + 1 
    if cnt <= K:
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
    # for _ in range(10**4):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

N, K = map(int,input().split())
A = list(map(int,input().split()))
ok = meguru_bisect(0, 2 * 10 ** 9)
ans = 0
for i in range(N):
    if A[i] >= ok:
        n = A[i] - ok + 1
        ans += n * (A[i] + ok) // 2
        K -= n
if K > 0:
    ans += K * (ok - 1)
print(ans)
