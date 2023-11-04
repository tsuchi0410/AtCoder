import itertools
from collections import Counter
N = input()
L = ["3", "5", "7"]
ans = 0
for i in range(1, len(N) + 1):
    all = itertools.product(L, repeat = i)
    for j in all:
        num = "".join(j)
        dic = Counter(num)
        num = int(num)
        if num <= int(N) and len(dic) == 3:
            ans += 1
print(ans)