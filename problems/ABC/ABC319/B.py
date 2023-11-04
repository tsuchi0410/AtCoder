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

N = int(input())
L = f(N)
ans = []
for i in range(0, N + 1):
    cnt = 0
    for j in L:
        if j >= 10:
            break
        if i % (N // j) == 0:
            cnt = j
            break
    if cnt == 0:
        ans.append("-")
    else:
        ans.append(str(cnt))

print("".join(ans))