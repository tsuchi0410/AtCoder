# エラトステネスの篩(素数の列挙)(O(NloglogN))
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

Q = int(input())
N = 10 ** 5
res = primes(N)
st = set(res)
L = [0] * N
for i in range(1, N, 2):
    if i in st and ((i + 1) // 2) in st:
        L[i] = 1
S = [0]
for i in range(N):
    S.append(S[i] + L[i])

for _ in range(Q):
    l, r = map(int,input().split())
    print(S[r + 1] - S[l])