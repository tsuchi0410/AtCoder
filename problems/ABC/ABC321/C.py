from collections import deque

K = int(input())

# 探索する範囲
d = set()

# 始点
q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(1, 10):
    d.add(i)

ans = []
while q:
    v = q.popleft()
    ans.append(v)

    num = str(v)
    num = num[-1]
    num = int(num)
    
    # 次見る場所
    next = []
    for i in range(num):
        if i < num:
            a = str(v) + str(i)
            a = int(a)
            if i != 0:
                next.append(a)
            else:
                ans.append(a)

    # 有向辺を貼りながらBFS
    for i in next:
        if not i in d:
            d.add(i)
            q.append(i)

ans.sort()
print(ans[K - 1])