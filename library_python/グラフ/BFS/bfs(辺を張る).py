from collections import deque

N = int(input())

# 探索する範囲
d = [-1] * (?)

# 始点
d[1] = 0
q = deque([1])

while q:
    v = q.popleft()
    
    # 次見る場所
    next = ?

    # 有向辺を貼りながらBFS
    if 条件 and d[next] == -1:
        d[next] = d[v] + 1
        q.append(next)


