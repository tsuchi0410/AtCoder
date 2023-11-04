from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from collections import defaultdict

N = int(input())
Q = int(input())
hako = defaultdict(SortedList)
card = defaultdict(SortedSet)
for _ in range(Q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        num, i, j = op
        hako[j].add(i)
        card[i].add(j)
    if op[0] == 2:
        num, i = op
        print(*hako[i])
    if op[0] == 3:
        num, i = op
        print(*card[i])