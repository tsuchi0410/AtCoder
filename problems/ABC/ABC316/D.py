from collections import deque
from collections import defaultdict
                
H, W = map(int, input().split())
c = [input() for _ in range(H)]

dic_h = defaultdict(defaultdict)
dic_w = defaultdict(defaultdict)
for i in range(H):
    for j in range(W):
        dic_h[i][c[i][j]] += 1
        dic_w[j][c[i][j]] += 1

print(dic_h)
print(dic_w)