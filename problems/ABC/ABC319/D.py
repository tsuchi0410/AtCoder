def is_ok(w):
    for i in range(N):
        if L[i] > w:
            return False
    ans = 1
    cnt = L[0]
    for i in range(1, N):
        if cnt + 1 + L[i] == w:
            cnt = 0
            if i != N - 1:
                ans += 1
        elif cnt + 1 + L[i] <= w:
            cnt += 1 + L[i]
        else:
            cnt = L[i]
            ans += 1
    if ans <= M:
        return True
    else:
        return False


def meguru_bisect(ng, ok):
    # for _ in range(10**4):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

N, M = map(int, input().split())
L = list(map(int, input().split()))

ans = meguru_bisect(0, 10**18)
print(ans)