from collections import deque

INF = 10 ** 10
vec_h = [-2, -1, 0, 1, 2]
vec_w = [-2, -1, 0, 1, 2]

def bfs(H, W, sh, sw, gh, gw):
    # deque にスタート位置を設定
    q = deque([[sh, sw]])
    # 深さを INF に初期化
    d = [[INF] * W for _ in range(H)]
    d[sh][sw] = 0
    # 深さを調整
    H -= 1
    W -= 1
    while q:
        y, x = q.popleft()
        
        if y == gh and x == gw:
            print(d[y][x])
            exit()

        for i in vec_h:
            for j in vec_w:
                
                next_i = y + i
                next_j = x + j
                
                if abs(i) + abs(j) >= 2:
                    cost = 1
                else:
                    cost = 0
                
                if not (0 <= next_i <= H and 0 <= next_j <= W) or S[next_i][next_j] == "#":
                    continue
                if i == 0 and j == 0:
                    continue
                
                # 隣接しているとき、左に append
                if cost == 0:
                    if d[next_i][next_j] > d[y][x] + cost:
                        d[next_i][next_j] = d[y][x] + cost
                        q.appendleft([next_i, next_j])
                else:
                    if d[next_i][next_j] > d[y][x] + cost:
                        d[next_i][next_j] = d[y][x] + cost
                        q.append([next_i, next_j])

    return print(-1)


H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())
S = [input() for _ in range(H)]

seen = [[False] * W for _ in range(H)]
bfs(H, W, Ch-1, Cw-1, Dh-1, Dw-1)