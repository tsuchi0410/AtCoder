import math
s = [input() for _ in range(9)]

rc = []
for i in range(9):
    for j in range(9):
        if s[i][j] == '#':
            rc.append([i,j])

ans = 0
for a in range(len(rc)):
    for b in range(a+1, len(rc)):
        for c in range(b+1, len(rc)):
            for d in range(c+1, len(rc)):
                
                ab = math.sqrt(((rc[a][0] - rc[b][0]) ** 2) + ((rc[a][1] - rc[b][1]) ** 2))
                ac = math.sqrt(((rc[a][0] - rc[c][0]) ** 2) + ((rc[a][1] - rc[c][1]) ** 2))
                bd = math.sqrt(((rc[b][0] - rc[d][0]) ** 2) + ((rc[b][1] - rc[d][1]) ** 2))
                cd = math.sqrt(((rc[c][0] - rc[d][0]) ** 2) + ((rc[c][1] - rc[d][1]) ** 2))
                
                ad = math.sqrt(((rc[a][0] - rc[d][0]) ** 2) + ((rc[a][1] - rc[d][1]) ** 2))
                bc = math.sqrt(((rc[b][0] - rc[c][0]) ** 2) + ((rc[b][1] - rc[c][1]) ** 2))
                if ab == ac and ab == bd and ab == cd:
                    if ad == bc:
                        ans += 1                    
print(ans)

