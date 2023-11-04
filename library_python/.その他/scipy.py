### Pythonで提出！###

# 関数の最小値
import math
from scipy import optimize
a, b = (int(x) for x in input().split())

def f(x):
    return b * x + a / (math.sqrt(x + 1))

res = optimize.fminbound(f, 0.000000, a, xtol = 1e-7, full_output=1)

r = int(res[0])
ans = float('inf')
for i in range(r-5, r+5, 1):
    if i < 0:
        continue
    ans = min(ans, f(i))
print(ans)