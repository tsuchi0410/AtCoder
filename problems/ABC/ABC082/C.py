from collections import Counter
N = int(input())
a = list(map(int,input().split()))
C = Counter(a)
ans = 0
for key, val in C.items():
    if val > key:
        ans += val - key
    elif val < key:
        ans += val
print(ans)