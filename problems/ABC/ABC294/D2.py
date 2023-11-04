from sortedcontainers import SortedList

N, Q = map(int, input().split())
S = SortedList([])
p = 1
for _ in range(Q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        S.add(p)
        p += 1
    elif event[0] == 2:
        S.discard(event[1])
    else:
        print(S[0])