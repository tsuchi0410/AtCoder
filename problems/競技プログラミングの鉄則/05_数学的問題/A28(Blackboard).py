N = int(input())
MOD = 10000
ans = 0
for _ in range(N):
    T, A = input().split()
    A = int(A)
    if T == "+": ans += A
    elif T == "-": ans -= A
    else: ans *= A
    ans %= MOD
    print(ans)