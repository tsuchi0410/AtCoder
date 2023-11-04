from collections import defaultdict, deque
n = int(input())
graph = defaultdict(list)
for _ in range(n) :
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
que = deque()
que.append(1)
S = {1}
while que:
	v = que.popleft()
	for i in graph[v]:
		if not i in S:
			que.append(i)
			S.add(i)
print(max(S))

print(graph)