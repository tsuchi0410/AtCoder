import sys
sys.setrecursionlimit(10 ** 6)
vec_x = [-1, 1, 0, 0]
vec_y = [0, 0, -1, 1]

def rec(v, seen, p):
    # 頂点 v を黒く塗る
    seen[v[0]][v[1]] = p
    
    for i in range(len(vec_x)):
        if v[0]+vec_x[i] < 0 or v[1]+vec_y[i] < 0:
            continue
        if v[0]+vec_x[i] >= h or v[1]+vec_y[i] >= w:
            continue
        if seen[v[0]+vec_x[i]][v[1]+vec_y[i]] != False:
            continue

        if c[v[0]+vec_x[i]][v[1]+vec_y[i]] == '.':
            v2 = [v[0]+vec_x[i], v[1]+vec_y[i]]
            p += 1
            rec(v2, seen, p)
    
    return seen
        
h, w = (int(x) for x in input().split())
c = [input() for _ in range(h)]
seen = [[False] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if c[i][j] == 'S':
            v = [i, j]

rec(v, seen, 1)
print('No')