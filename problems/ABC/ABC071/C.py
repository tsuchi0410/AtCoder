from collections import Counter
N = int(input())
A = list(map(int,input().split()))
C = Counter(A)
print(C)
ans = 0
for key, val in C.items():
    if val >= 4:
        ans = max(ans, key * key)
L = []
for key, val in C.items():
    if val >= 2:
        L.append(key)

L.sort(reverse = True)

if len(L) >= 2:
    ans = max(ans, L[0] * L[1])
print(ans)