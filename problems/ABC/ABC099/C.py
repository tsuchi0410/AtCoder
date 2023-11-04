from collections import deque

N = int(input())

# 探索する範囲
d = [-1] * (10 ** 5 + 10)

# 始点
d[0] = 0
q = deque([0])

while q:
    v = q.popleft()
    
    # 次見る場所
    # 9**5
    # 6**6
    l = [v + 1]
    for i in range(1, 6):
        l.append(v + 9 ** i)
    for i in range(1, 7):
        l.append(v + 6 ** i)

    # 有向辺を貼りながらBFS
    for next in l:
        if next <= 10 ** 5 and d[next] == -1:
            d[next] = d[v] + 1
            q.append(next)

print(d[N])
