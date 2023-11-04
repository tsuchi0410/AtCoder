n = int(input())
MOD = 10 ** 9 + 7
a = []
for i in range(n):
    l = list(map(int,input().split()))
    a.append(l)

ans = 0
for i in range(n):
    if i == 0:
        ans = sum(a[i]) % MOD
    else:
        ans = ans * sum(a[i]) % MOD
print(ans % MOD)