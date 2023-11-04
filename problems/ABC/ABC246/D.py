N = int(input())
# X = a^3 + a^2b + ab^2+b^3

if N == 0:
    print(0)
    exit()

ans = float("inf")
for a in range(10 ** 6 + 10):
    ng = 0
    ok = 10 ** 6 + 10
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        X = a ** 3 + a ** 2 * mid + a * mid ** 2 + mid ** 3
        if X < N:
            is_ok = False
        else:
            is_ok = True
        if is_ok == True:
            ok = mid
        else:
            ng = mid
    
    X = a ** 3 + a ** 2 * ok + a * ok ** 2 + ok ** 3
    ans = min(ans, X)

print(ans)