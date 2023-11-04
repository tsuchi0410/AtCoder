import sys
sys.setrecursionlimit(10 ** 6)

vec_x = [-1, 1, 0, 0]
vec_y = [0, 0, -1, 1]

def rec(v, seen):
    # 頂点 v を黒く塗る
    seen[v[0]][v[1]] = True
    
    for i in range(len(vec_x)):
        if seen[v[0]+vec_x[i]][v[1]+vec_y[i]] == True:
            continue
        if g[v[0]+vec_x[i]][v[1]+vec_y[i]] == 1:
            v2 = [v[0]+vec_x[i], v[1]+vec_y[i]]
            rec(v2, seen)
    
        
h, w = (int(x) for x in input().split())
g = [[0] * 110 for _ in range(110)]
s = []
seen = [[False] * 110 for _ in range(110)]
grid = [input() for _ in range(h)]
for i in range(h):
    for j in range(w):
        
        if grid[i][j] == '#':
            g[i][j] = 1
            # スタート地点の候補
            s.append([i, j])
    
ans = 0
for i in range(len(s)):
    if seen[s[i][0]][s[i][1]] == False:
        rec(s[i], seen)
        ans += 1

print(ans)
