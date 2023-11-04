import math
n = int(input())
x, y = (int(x) for x in input().split())
xx, yy = (int(x) for x in input().split())

a = (xx + x) / 2
b = (yy + y) / 2
x -= a
y -= b
r = math.sqrt(((xx - x) ** 2) + ((yy - y) ** 2)) / 2
theta = 360 / n
theta = math.radians(theta)

x1 = x * math.cos(theta) - y * math.sin(theta)
y1 = x * math.sin(theta) + y * math.cos(theta)

print(x1 + a, y1 + b)
