# どの異なる 5 個の整数を選んでも合成数になる
# 1 (mod 5) となる数を選べばよい 

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

N = int(input())
res = primes(10 ** 5)
ans = []
for i in res:
    if i % 5 == 1:
        ans.append(i)
    if len(ans) == N:
        print(*ans, sep = " ")
        exit()