import math
a, b = (int(x) for x in input().split())


#(1)最小にしたい関数fを定義する
def f(x):
    return b * x + a / (math.sqrt(x + 1))

#(2)関数fの最小値を探したい閉区間の両端をl,rと置く(l<=r)
l, r = 0, a
while r - l > 1:
    #(4)オーバーフローしないように以下のように三等分点を置く
    c1 = l + (r - l) / 3
    c2 = r - (r - l) / 3
    #(5)更新を行う
    if f(c1) < f(c2):
        r = c2
    else:
        l = c1

r = int(r)
ans = float('inf')
for i in range(r-5, r+5, 1):
    if i < 0:
        continue
    ans = min(ans, f(i))

print(ans)
