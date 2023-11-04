from collections import deque
vec = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())
S = [input() for _ in range(N)]

# スタート位置
sh, sw = 1, 1

d = [[False] * M for _ in range(N)]
d[sh][sw] = True
seen = [[False] * M for _ in range(N)]
seen[sh][sw] = True

# deque にスタート位置を設定
q = deque([[sh, sw]])

while q:
    y, x = q.popleft()
    for i in range(4):
        y2 = y + vec[i][0]
        x2 = x + vec[i][1]
        while True:
            if S[y2][x2] == '.':
                d[y2][x2] = True
                y2 += vec[i][0]
                x2 += vec[i][1] 
            else:
                if seen[y2 - vec[i][0]][x2 - vec[i][1]] == False:
                    q.append([y2 - vec[i][0], x2 - vec[i][1]])
                    seen[y2 - vec[i][0]][x2 - vec[i][1]] = True
                break

ans = 0
for i in d:
    ans += i.count(True)
print(ans)