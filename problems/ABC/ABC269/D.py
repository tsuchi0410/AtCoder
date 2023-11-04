import sys
sys.setrecursionlimit(10 ** 6)

vec_x = [-1, -1, 0, 0, 1, 1]
vec_y = [-1, 0, -1, 1, 0, 1]

def rec(v, seen):
    # 頂点 v を黒く塗る
    seen[v[0]][v[1]] = True
    
    for i in range(len(vec_x)):
        if seen[v[0]+vec_x[i]][v[1]+vec_y[i]] == True:
            continue
        if g[v[0]+vec_x[i]][v[1]+vec_y[i]] == 1:
            v2 = [v[0]+vec_x[i], v[1]+vec_y[i]]
            rec(v2, seen)
    
        
n = int(input())
g = [[0] * 3000 for _ in range(3000)]
s = []
seen = [[False] * 3000 for _ in range(3000)]
for i in range(n):
    x, y = list(map(int,input().split()))
    
    # 入力に負の値が含まれる時があるので余裕を持つ
    x += 1000; y += 1000
    g[x][y] = 1
    
    # スタート地点の候補
    s.append([x, y])


ans = 0
for i in range(len(s)):
    if seen[s[i][0]][s[i][1]] == False:
        seen[s[i][0]][s[i][1]] = True
        rec(s[i], seen)
        ans += 1
    

print(ans)
