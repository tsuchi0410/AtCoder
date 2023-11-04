from collections import defaultdict
n = int(input())
a = list(map(int,input().split()))

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

d = defaultdict(int)
for i in a:
    d[i] += 1

# 約数列挙
yakusu = defaultdict(list)
for i in d:
    y = make_divisors(i)
    yakusu[i] = y
    
ans = 0
for i in d:
    for j in yakusu[i]:
        k = i // j
        if j in d and k in d:
                ans += d[i] * d[j] * d[k]

print(ans)