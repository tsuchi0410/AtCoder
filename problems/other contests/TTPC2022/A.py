x, y = (int(x) for x in input().split())

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

a = make_divisors(y-x)
b = make_divisors(x-2015)
a = set(a); b = set(b)
ans = list(a & b)
ans.sort()
print(*ans, sep = '\n')