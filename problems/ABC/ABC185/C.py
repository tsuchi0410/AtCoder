import math
L = int(input())
print(math.comb(L, 12) - math.comb(L - 1, 12))