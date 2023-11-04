from collections import deque

def mod_pow(x, n, mod):
    if n == 0:
        return 1
    res = mod_pow(x**2 % mod, n//2, mod)
    if n & 1:
        # nが奇数ならxを掛ける
        res = res * x % mod
    return res

Q = int(input())
S = deque([1])
MOD = 998244353
ans = 1
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        op, x = q
        ans *= 10
        ans += x
        S.append(x)
    elif q[0] == 2:
        ans -= S[0] * mod_pow(10, (len(S)-1), MOD)
        S.popleft()
    else:
        print(ans)

    ans %= MOD