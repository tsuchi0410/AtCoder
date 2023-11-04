h, w = map(int, input().split())
c = [input() for _ in range(h)]
cnt = []
for col in zip(*c):
    cnt.append(col.count('#'))

print(*cnt)