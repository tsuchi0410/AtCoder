from collections import defaultdict
N, K = map(int, input().split())
dic = defaultdict(int)
for _ in range(N):
    a, b = map(int, input().split())
    dic[a] += b
l = []
for k, v in dic.items():
    l.append([k, v])
l.sort()
for k, v in l:
    if K - v > 0:
        K -= v
    else:
        print(k)
        exit()