import itertools
from collections import Counter
import math

def rcomb(n, r):
    return math.comb(n + r - 1, r)

N, T, M = map(int, input().split())
L = []
for _ in range(M):
    A, B = map(int, input().split())
    L.append([A, B])

NMAX = 0
for i in range(10):
    if 1 * (T - 1) + i == N:
        NMAX = i

all = itertools.combinations_with_replacement(list(range(1, NMAX + 1)), T)
S = set()
for i in all:
    if sum(i) == N:
        S.add(i)

ans = 0
for i in S:
    dic = Counter(i)
    p = N
    buf = 0
    for k, v in dic.items():
        buf2 = 1
        for j in range(v):
            buf2 *= rcomb(p, k)
            p -= k
        buf *= buf2 // math.factorial(v)
        print(buf)
    
    ans += buf
    #print(ans)

print(ans)