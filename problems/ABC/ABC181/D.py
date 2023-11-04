from collections import defaultdict
import itertools
S = input()
d = defaultdict(int)
l = []
for i in range(len(S)):
    d[S[i]] += 1
    if d[S[i]] <= 3:
        l.append(S[i])

if len(S) == 1:
    if int(S) % 8 == 0:
        print("Yes")
        exit()
elif len(S) == 2:
    cmb = list(itertools.combinations(l, 2))
    for i in cmb:
        ll = list(itertools.permutations(i))
        for j in ll:
            ans = ""
            for k in j:
                ans += k
            if int(ans) % 8 == 0:
                print("Yes")
                exit()
else:
    cmb = list(itertools.combinations(l, 3))
    for i in cmb:
        ll = list(itertools.permutations(i))
        for j in ll:
            ans = ""
            for k in j:
                ans += k
            if int(ans) % 8 == 0:
                print("Yes")
                exit()
print("No")
