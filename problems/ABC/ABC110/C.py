from collections import defaultdict
S = input()
T = input()
d1 = defaultdict(list)
d2 = defaultdict(list)
N = len(S)
for i in range(N):
    d1[S[i]].append(i)
    d2[T[i]].append(i)
l1 = []
l2 = []
for k, v in d1.items():
    l1.append(v)
for k, v in d2.items():
    l2.append(v)
l1.sort()
l2.sort()
if l1 == l2:
    print("Yes")
else:
    print("No")