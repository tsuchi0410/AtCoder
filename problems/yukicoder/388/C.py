N, A, B = map(int,input().split())
MOD = 998244353
ans = 0
u = 1
for i in range(N, 0, -1):
    u *= i
    u %= MOD
x = 1
for i in range(N-1, 0, -1):
    x *= i
    x %= MOD
y = 1
for i in range(N-1, 0, -1):
    y *= i
    y %= MOD
x_and_y = 1
if A == B:
    x_and_y = 0
else:
    for i in range(N-2, 0, -1):
        x_and_y *= i
        x_and_y %= MOD
ans = u - (x + y - x_and_y)
print(ans % MOD)