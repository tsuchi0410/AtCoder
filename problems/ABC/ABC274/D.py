n, x, y = (int(x) for x in input().split())
a = list(map(int,input().split()))

# 全探索だと、次は2通りなのでO(2^N)
# 線分のなす角は90°なので1回の移動ごとにx座標とy座標が入れかわる
    # ⇔ i回目の動作では、iが奇数ならばx座標での移動を行い、そうでなければy座標での移動を行う
# この判定問題はx座標とy座標でわけて考えられる

dpx = []; dpy = []; #inf = 2 * (10 ** 4) + 1
inf = 10
for i in range(n+1):
    dpx.append([False] * inf)
    dpy.append([False] * inf)

# 初期値
dpx[0][0] = True; dpy[0][0] = True
dpx[1][a[0]] = True; dpy[1][0] = True

for i in range(2, n+1):
    for j in range(inf):
        
        if i == n:
            continue
        
        # 偶数（y座標）
        if i % 2 == 0:
            if dpy[i][j] == True:
                dpy[i+1][j+a[i-1]] = True
                dpy[i+1][j-a[i-1]] = True
            dpx[i+1][j] = dpx[i][j]
        else:
            # 奇数（x座標)
            if dpx[i][j] == True:
                dpx[i+1][j+a[i-1]] = True
                dpx[i+1][j-a[i-1]] = True
            dpy[i+1][j] = dpy[i][j]

if dpx[-1][x] == True and dpy[-1][y] == True:
    print('Yes')
else:
    print('No')

print(dpx)
print(dpy)
