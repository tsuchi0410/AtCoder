"""
円の中心(ox, oy) と、(x, y) の距離 = 半径
1/2 乗は誤差が怖いので、2乗距離で判定
"""

def ed(xa, ya, xb, yb):
    return (xa - xb) ** 2 + (ya - yb) ** 2


if ed(ox, oy, x, y) == R ** 2:


"""
座標 (x, y) が 円の内側に存在する
"""

if ed(ox, oy, x, y) < R ** 2:


"""
座標 (x, y) が 円の外側に存在する
"""

if ed(ox, oy, x, y) > R ** 2: