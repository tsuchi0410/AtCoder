import math
a, b, c = (int(x) for x in input().split())

l = math.gcd(a, b)
l = math.gcd(l, c)

ans = 0
ans += (a // l) - 1
ans += (b // l) - 1
ans += (c // l) - 1

print(int(ans))