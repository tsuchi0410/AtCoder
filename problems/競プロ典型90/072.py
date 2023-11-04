import sys
sys.setrecursionlimit(10**7) # 再起回数の設定

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
seen = [[False] * W for _ in range(H)] # 状態を管理
vec = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 移動先

def dfs(goal_h, goal_w, now_h, now_w):
    # すべて探索した
    if goal_h == now_h and goal_w == now_w and seen[now_h][now_w] == True:
        return 0
    seen[now_h][now_w] = True # 探索スタート
    
    res = float("inf") * (-1)
    for dh, dw in vec:
        next_h = dh + now_h
        next_w = dw + now_w

        # 境界値と壁の確認
        if not (0 <= next_h < H and 0 <= next_w < W and maze[next_h][next_w] == "."):
            continue
        # ゴールはしてないが探索済み
        if not(goal_h == next_h and goal_w == next_w) and seen[next_h][next_w] == True:
            continue

        res = max(res, dfs(goal_h, goal_w, next_h, next_w) + 1)
    
    # 探索が終わったら履歴を破棄
    seen[now_h][now_w] = False
    return res

ans = -1
for h in range(H):
    for w in range(W):
        if maze[h][w] == ".":
            ans = max(ans, dfs(h, w, h, w))

if ans <= 2: # 往復は不適切 
    print(-1)
else:
    print(ans)