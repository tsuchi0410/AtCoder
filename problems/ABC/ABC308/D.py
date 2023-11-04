from collections import deque

L = "snuke"

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
        if S[y][x] in L:
            now = L.index(S[y][x])
        else:
            continue

        # ゴールに到着したら終了
        if y == gh and x == gw:
            break
                
        for i, j in [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]:
            
            if i < 0 or j < 0:
                continue
            if i > H or j > W:
                continue
            
            next = L[(now + 1) % 5]
            if d[i][j] == -1 and S[i][j] == next:
                q.append([i, j])
                d[i][j] = d[y][x] + 1
                
    return d

# 入力
H, W = (int(x) for x in input().split())
S = [input() for _ in range(H)]

# スタート位置
sh, sw = 0, 0

# ゴール位置
gh, gw = H, W

# bfs
d = bfs(H, W, sh, sw, gh, gw)
if d[H - 1][W - 1] == -1:
    print("No")
else:
    print("Yes")