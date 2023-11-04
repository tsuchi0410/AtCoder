import math
a, b = (int(x) for x in input().split())
ans = a * b // math.gcd(a, b)
if ans > 10 ** 18:
    print("Large")
else:
    print(ans)