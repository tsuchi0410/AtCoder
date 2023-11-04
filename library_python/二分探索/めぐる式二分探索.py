def is_ok(mid):

def meguru_bisect(ng, ok):
    # for _ in range(10**4):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok