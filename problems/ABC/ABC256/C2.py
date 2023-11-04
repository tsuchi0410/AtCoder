h1, h2, h3, w1, w2, w3 = (int(x) for x in input().split())

ans = 0
for i in range(1, 30):
    for j in range(1, 30):
        for k in range(1, 30):
            for l in range(1, 30):
                
                a = h1-j-i
                b = h2-l-k
                e = w1-i-k
                d = w2-j-l
                c1 = w3-a-b
                c2 = h3-e-d
            
                if min(a,b,d,e) > 0:
                    if c1 == c2 and c1 > 0:
                        ans += 1

print(ans)
