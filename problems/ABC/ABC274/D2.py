n, x, y = (int(x) for x in input().split())
a = list(map(int,input().split()))

# 全探索だと、次は2通りなのでO(2^N)
# 線分のなす角は90°なので1回の移動ごとにx座標とy座標が入れかわる
    # ⇔ i回目の動作では、iが奇数ならばx座標での移動を行い、そうでなければy座標での移動を行う
# この判定問題はx座標とy座標でわけて考えられる

# setで動的計画法を行う
# 負の値を考慮しなくていいので楽
dpx = []; dpy = []
for i in range(n+1):
    dpx.append(set())
    dpy.append(set())

# 初期値
dpx[0].add(0); dpy[0].add(0)
dpx[1].add(a[0]); dpy[1].add(0)

for i in range(1, n+1):
    
    if i == n:
        continue
    
    # 次が偶数（y座標）
    if i % 2 == 1:
        for j in dpy[i]:
            dpy[i+1].add(j+a[i])
            dpy[i+1].add(j-a[i])
        dpx[i+1] = dpx[i]
    else:
        # 次が奇数（x座標)
        for j in dpx[i]:
            dpx[i+1].add(j+a[i])
            dpx[i+1].add(j-a[i])
        dpy[i+1] = dpy[i]

if x in dpx[-1] and y in dpy[-1]:
    print('Yes')
else:
    print('No')
