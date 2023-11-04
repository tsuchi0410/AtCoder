import heapq
from collections import deque

Q = int(input())
q = deque([])
hq = []
heapq.heapify(hq)
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        q.append(x)
    elif query[0] == 2:
        if len(hq) == 0:
            res = q.popleft()
            print(res)
        else:
            res = heapq.heappop(hq)
            print(res)
    elif query[0] == 3:
        while q:
            res = q.popleft()
            heapq.heappush(hq, res)
        q = deque([])
    
