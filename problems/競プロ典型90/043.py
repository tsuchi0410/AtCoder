from collections import deque

def bfs(H, W, sh, sw, gh, gw):
    
    # 深さを -1 に初期化
    d = [[-1] * W for _ in range(H)]
    d[sh][sw] = 0
    
    # deque にスタート位置を設定
    q = deque([[sh, sw]])
    
    # 境界の調整
    H -= 1
    W -= 1
    
    while q:
        y, x = q.popleft()
    
        # ゴールに到着したら終了
        if y == gh and x == gw:
            break
                
        for i, j in [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]:
            
            if i < 0 or j < 0:
                continue
            if i > H or j > W:
                continue
            
            if d[i][j] == -1 and S[i][j] == '.':
                q.append([i, j])
                d[i][j] = d[y][x] + 1
                
    return d


H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
S = [input() for _ in range(H)]
rs -= 1
cs -= 1
rt -= 1
ct -= 1
d = bfs(H, W, rs, cs, rt, ct)
for i in d:
    print(i)