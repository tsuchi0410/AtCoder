N, M = map(int, input().split())

ans = -1
num = []
# (x + y) % MOD = ((x % MOD) + (y % MOD)) % MOD
# (x * y) % MOD = ((x % MOD) * (y % MOD)) % MOD
for i in range(N):
    for j in range(9):
        if i == 0:
            num.append((j + 1) % M)
            if (j + 1) % M == 0:
                ans = [1, j + 1]
        else:
            num[j] = num[j] * (10 % M)
            num[j] %= M
            num[j] = num[j] + ((j + 1) % M)
            num[j] %= M
            if num[j] == 0:
                ans = [i + 1, j + 1]

if ans == -1:
    print(ans)
else:
    l = []
    for i in range(ans[0]):
        l.append(str(ans[1]))
    print("".join(l))