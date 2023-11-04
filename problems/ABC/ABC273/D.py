import bisect
from collections import defaultdict

h, w, rs, cs = (int(x) for x in input().split())
n = int(input())
rc = []
for i in range(n):
    r, c = (int(x) for x in input().split())
    rc.append([r, c])
q = int(input())
dl = []
for i in range(q):
    d, l = (x for x in input().split())
    dl.append([d, int(l)])


d1 = defaultdict(list)
d2 = defaultdict(list)
for i in rc:
    d1[i[0]].append(i[1])
    d2[i[1]].append(i[0])

for i in d1:
    d1[i] = sorted(d1[i])

for i in d2:
    d2[i] = sorted(d2[i])


for i in range(q):
        
    if dl[i][0] == 'L':
        
        # 同じ高さに壁がある
        if rs in d1:
            next_cs = cs - dl[i][1]
            if next_cs < 1:
                next_cs = 1
            
            now_idx = bisect.bisect_left(d1[rs], cs)
            next_idx = bisect.bisect_left(d1[rs], next_cs)
            
            # 道中に障害物はない
            if now_idx == next_idx:
                cs = next_cs
            # あった
            else:
                cs = d1[rs][now_idx-1] + 1
        
        else:
            next_cs = cs - dl[i][1]
            if next_cs < 1:
                next_cs = 1
            cs = next_cs
    
    if dl[i][0] == 'R':
        
        # 同じ高さに壁がある
        if rs in d1:
            next_cs = cs + dl[i][1]
            if next_cs > w:
                next_cs = w
            
            now_idx = bisect.bisect_right(d1[rs], cs)
            next_idx = bisect.bisect_right(d1[rs], next_cs)
            
            # 道中に障害物はない
            if now_idx == next_idx:
                cs = next_cs
            # あった
            else:
                cs = d1[rs][now_idx] - 1
        else:
            next_cs = cs + dl[i][1]
            if next_cs > w:
                next_cs = w
            cs = next_cs
                
    if dl[i][0] == 'U':
        
        # 縦列に障害物がある
        if cs in d2:
            next_rs = rs - dl[i][1]
            if next_rs < 1:
                next_rs = 1
            
            now_idx = bisect.bisect_left(d2[cs], rs)
            next_idx = bisect.bisect_left(d2[cs], next_rs)
            
            # 道中に障害物はない
            if now_idx == next_idx:
                rs = next_rs
            # あった
            else:
                rs = d2[cs][now_idx-1] + 1
        else:
            next_rs = rs - dl[i][1]
            if next_rs < 1:
                next_rs = 1
            rs = next_rs
                
    if dl[i][0] == 'D':
        
        # 縦列に障害物がある
        if cs in d2:
            next_rs = rs + dl[i][1]
            if next_rs > h:
                next_rs = h
            
            now_idx = bisect.bisect_right(d2[cs], rs)
            next_idx = bisect.bisect_right(d2[cs], next_rs)
            
            # 道中に障害物はない
            if now_idx == next_idx:
                rs = next_rs
            # あった
            else:
                rs = d2[cs][now_idx] - 1
        else:
            next_rs = rs + dl[i][1]
            if next_rs > h:
                next_rs = h
            rs = next_rs

    print(rs, cs)