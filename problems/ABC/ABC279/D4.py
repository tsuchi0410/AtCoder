import math
from scipy import optimize
a, b = (int(x) for x in input().split())

def f(x):
    return b * x + a / (math.sqrt(x + 1))

res = optimize.fminbound(f, 0.000000, a, xtol = 1e-7, full_output=1)
print(res[1])