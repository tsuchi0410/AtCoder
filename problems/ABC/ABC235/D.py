from collections import deque
a, N = map(int, input().split())

# 桁数を管理
M = 1
while M <= N:
    M *= 10

d = [-1] * (M + 1)
d[1] = 0
q = deque([1])

while q:
    v = q.popleft()
    
    # 操作1
    op1 = v * a
    if op1 < M and d[op1] == -1:
        d[op1] = d[v] + 1
        q.append(op1)
    
    # 操作2
    if v >= 10 and v % 10 != 0:
        op2 = str(v)
        op2 = op2[-1] + op2[:-1]
        op2 = int(op2)
        if op2 < M and d[op2] == -1:
            d[op2] = d[v] + 1
            q.append(op2)

print(d[N])

