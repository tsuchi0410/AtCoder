import heapq
n, k = (int(x) for x in input().split())
p = list(map(int,input().split()))

p2 = p[0:k]
heapq.heapify(p2)

print(p2[0])
for i in range(k, n):
    
    if p2[0] < p[i]:
        heapq.heappop(p2)
        heapq.heappush(p2, p[i])
    
    print(p2[0])