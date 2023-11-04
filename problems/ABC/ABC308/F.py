import bisect
import heapq

N, M = map(int, input().split())
P = list(map(int, input().split()))
L = list(map(int, input().split()))
D = list(map(int, input().split()))

dic = {}
for i in range(M):
    if L[i] in dic:
        dic[L[i]].append(-D[i])
    else:
        dic[L[i]] = [-D[i]]
for k in dic.keys():
    heapq.heapify(dic[k])  

P.sort()
Ps = {}
for i in P:
    if i in Ps:
        Ps[i] += 1
    else:
        Ps[i] = 1

cnt = 0
for k, v in dic.items():
    while len(v):
        idx = bisect.bisect_left(P, k)
        if idx > len(P):
            break
        else:
            if Ps[P[idx]] > 0:
                num = -1 * heapq.heappop(v)
                cnt += num
                Ps[P[idx]] -= 1
            else:
                break

print(sum(P) - cnt)