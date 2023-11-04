# 長方形の存在判定
# 対角線上の頂点を決める

n = int(input())
s = set()
p = []
for i in range(n):
    x, y = (int(x) for x in input().split())
    p.append([x,y])
    s.add((x,y))

ans = 0
for i in range(n):
    for j in range(i+1,n):
        x1, y1 = p[i][0], p[i][1]
        x2, y2 = p[j][0], p[j][1]
        
        # x座標同士とy座標同士が同じとき、対角線になり得ない
        if x1 == x2 or y1 == y2:
            continue
        
        if (x1, y2) in s and (x2, y1) in s:
            ans += 1
            
print(ans // 2)
