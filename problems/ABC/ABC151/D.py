from collections import deque

def bfs(H, W, sh, sw):
    
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

        for i, j in [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]:
            
            if i < 0 or j < 0:
                continue
            if i > H or j > W:
                continue
            
            if d[i][j] == -1 and S[i][j] == '.':
                q.append([i, j])
                d[i][j] = d[y][x] + 1
                
    return d

# 入力
H, W = (int(x) for x in input().split())
S = [input() for _ in range(H)]

# スタート位置
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            res = bfs(H, W, i, j)
            
            for k in res:
                ans = max(ans, max(k))

print(ans)