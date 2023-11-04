# 順列の総数 (1)
from math import factorial
res = factorial(N) // factorial(N - R)

# 順列の総数 (2)
# Python 3.8 で提出
# n 個から k 個選ぶとき、math.perm(n, k)
import math
res = math.perm(4, 2)

# 順列列挙
# 引数 = 何個選ぶか
lst = list(itertools.permutations([1, 2, 3], 3))
# -> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]



# 重複順列列挙
# repeat = 何個選ぶか
all = itertools.product([1, 2, 3], repeat = 3)
# => (1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), ... ,(3, 3, 2), (3, 3, 3)