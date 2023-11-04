import heapq
from collections import defaultdict
from collections import deque
q = int(input())
h = []
heapq.heapify(h)  
cnt = 0
x = [0]
d = defaultdict(deque)
for i in range(q):
    que = list(map(int,input().split()))
    if que[0] == 1:
        heapq.heappush(h,que[1])
        d[que[1]].append(cnt)
    elif que[0] == 3:
        a = heapq.heappop(h)
        num = d[a].popleft() 
        print(a + (x[cnt] - x[num]))
    else:
        cnt += 1
        x.append(x[cnt-1] + que[1])

