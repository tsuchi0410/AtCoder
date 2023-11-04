from collections import defaultdict
import itertools
S = input()
d = defaultdict(int)
for i in range(len(S)):
    d[S[i]] += 1

if len(S) == 1:
    if int(S) % 8 == 0:
        print("Yes")
        exit()

elif len(S) == 2:
    l = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    all = itertools.product(l, repeat = 2)
    ans = ""
    for i in all:
        for j in i:
            ans += j
    
    d2 = defaultdict(int)
    if int(ans) % 8 == 0:
        for i in all:
            d2[i] += 1

    f = True
    for i in d2:
        if d2[i] > d[i]:
            f = False
            break
    if f == True:
        print("Yes")
        exit()