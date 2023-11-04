from collections import defaultdict

H, W = map(int, input().split())
P = []
for i in range(H):
    p = list(map(int,input().split()))
    P.append(p)

ans = 0
BIT = H
for i in range(2 ** BIT):
    l = [i >> j & 1 for j in range(BIT)]

    G = []
    for j in range(len(l)):
        if l[j] == 1:
            G.append(P[j])
    
    dic = defaultdict(int)
    for col in zip(*G):
        # 1種類
        if len(set(col)) == 1:
            dic[col] += 1
    
    cnt = l.count(1)
    for v in dic.values():
        ans = max(ans, v * cnt)

print(ans)