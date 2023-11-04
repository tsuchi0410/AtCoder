from sortedcontainers import SortedList
from collections import defaultdict

N, M = map(int, input().split())
P = [0] * M
Y = [0] * M
for i in range(M):
    P[i], Y[i] = map(int, input().split())

dic = defaultdict(SortedList)
for i in range(M):
    dic[P[i]].add(Y[i])

for i in range(M):
    ans = str(P[i]).zfill(6) + str(dic[P[i]].index(Y[i]) + 1).zfill(6)
    print(ans)