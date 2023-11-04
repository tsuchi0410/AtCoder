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

K = int(input())
L = f(K)
N = len(L)
ans = 0
st = set(L)
for i in range(N):
    for j in range(i, N):
        if K % (L[i] * L[j]) == 0:
            num = K // (L[i] * L[j])
            if num in st and L[j] <= num:
                ans += 1
print(ans)
