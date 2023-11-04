# 座標の回転
import math
x1 = x * math.cos(theta) - y * math.sin(theta)
y1 = x * math.sin(theta) + y * math.cos(theta)

# 回転したい点が原点じゃないとき
# a, b 原点にしたい
a = (xx + x) / 2
b = (yy + y) / 2
x -= a
y -= b
x1 = x * math.cos(theta) - y * math.sin(theta)
y1 = x * math.sin(theta) + y * math.cos(theta)
x1 += a
y1 += b