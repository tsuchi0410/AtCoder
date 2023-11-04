N = int(input())

def f(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

d = {}
for ab in range(1, N):
    d[ab] = 0
    L = f(ab)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i] * L[j] == ab:
                d[ab] += 1

ans = 0
for ab in range(1, N):
    ans += d[ab] * d[N - ab]

print(ans)