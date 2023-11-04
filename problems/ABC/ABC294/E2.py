from collections import deque
L, N1, N2 = map(int, input().split())
A = deque([])
for i in range(N1):
    v, l = map(int, input().split())
    A.append([v, l])

B = deque([])
for i in range(N2):
    v, l = map(int, input().split())
    B.append([v, l])

cntA = 0
cntB = 0
ans = 0
while A or B:
    if cntA == cntB:
        v1, l1 = A.popleft()
        v2, l2 = B.popleft()
        if v1 == v2:
            ans += min(l1, l2)
        cntA += l1
        cntB += l2
    elif cntA < cntB:
        v1, l1 = A.popleft()
        if v1 == v2:
            ans += min(l1, cntB - cntA)
        cntA += l1
    else:
        v2, l2 = B.popleft()
        if v1 == v2:
            ans += min(l2, cntA - cntB)
        cntB += l2

print(ans)