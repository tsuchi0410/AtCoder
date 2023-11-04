n, a, b = (int(x) for x in input().split())
import math
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

def baisu_souwa(n, a):
    syokou = a
    kou = n // a
    makkou = kou * a
    ans = (syokou + makkou) * kou // 2
    return ans

s = (n * (n + 1)) // 2
n1 = baisu_souwa(n, a)
n2 = baisu_souwa(n, b)
n3 = baisu_souwa(n, a * b // math.gcd(a, b))
print(s - ((n1+n2)-n3))