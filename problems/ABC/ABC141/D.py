import heapq
n, m = map(int, input().split())
a = list(map(int,input().split()))
for i in range(n):
    a[i] *= -1

heapq.heapify(a)
for _ in range(m):
    a_max = -1 * heapq.heappop(a)
    a_max //= 2
    heapq.heappush(a, -1 * a_max)

ans = 0
for i in range(n):
    ans += -1 * heapq.heappop(a)

print(ans)