import heapq

N = int(input())
dic = {}
hq= []
for i in range(N):
    S, C = map(int, input().split())
    dic[S] = C
    hq.append(S)

heapq.heapify(hq)
while hq:
    S = heapq.heappop(hq)  
    C = dic[S]

    if C <= 1:
        continue

    # 次見る場所
    ns = S * 2
    nc = C // 2
    # dic管理
    if C % 2 == 0:
        dic[S] = 0
    else:
        dic[S] = 1
    # 有向辺を貼りながらBFS
    if nc >= 1:
        if ns in dic:
            dic[ns] += nc
        else:
            dic[ns] = nc
        heapq.heappush(hq, ns)

ans = 0
for k, v in dic.items():
    ans += v
print(ans)