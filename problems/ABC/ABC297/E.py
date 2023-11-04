import heapq
N, K = map(int,input().split())
A = list(map(int,input().split()))
hq = [0]
heapq.heapify(hq)
ans = set()
for i in range(K + 1):
    while True:
        num = heapq.heappop(hq)
        if num in ans:
            continue
        else:
            ans.add(num)
            break
    for j in range(N):
        heapq.heappush(hq, num + A[j])
print(num)
