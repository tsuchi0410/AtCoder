import bisect
INF = float("inf")
A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
for i in range(Q):
    ans = float("inf")
    x = int(input())
    idx = bisect.bisect_left(s, x)
    if idx == 0:
        ss = [-INF, s[0]]
    elif idx == A:
        ss = [s[-1], INF]
    else:
        ss = [s[idx - 1], s[idx]]
    idx = bisect.bisect_left(t, x)
    if idx == 0:
        tt = [-INF, t[0]]
    elif idx == B:
        tt = [t[-1], INF]
    else:
        tt = [t[idx - 1], t[idx]]
    
    # ll
    num = x - min(ss[0], tt[0])
    if num != -INF:
        ans = min(ans, num)
    # rr
    num = max(ss[1], tt[1]) - x
    if num != INF:
        ans = min(ans, num)
    # lr s -> t
    num = x - ss[0] + (tt[1] - ss[0])
    if num != -INF or num != INF:
        ans = min(ans, num)
    # lr t -> s
    num = x - tt[0] + (ss[1] - tt[0])
    if num != -INF or num != INF:
        ans = min(ans, num)
    # rl s -> t
    num = ss[1] - x + (ss[1] - tt[0])
    if num != -INF or num != INF:
        ans = min(ans, num)
    # rl t -> s
    num = tt[1] - x + (tt[1] - ss[0])
    if num != -INF or num != INF:
        ans = min(ans, num)

    print(ans)
