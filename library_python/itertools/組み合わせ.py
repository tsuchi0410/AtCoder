# 組み合わせの総数 (1)
from math import factorial
a = factorial(N) // (factorial(R) * factorial(N - R))

# 組み合わせの総数 (2)
# Python 3.8 で提出
import math
math.comb(n, k)

# 組み合わせ列挙
cmb = list(itertools.combinations([1, 2, 3], 2))
#=> (1, 2), (1, 3), (2, 3)



# 重複組み合わせの総数
# Python 3.8 で提出
import math

def rcomb(n, r):
    return math.comb(n + r - 1, r)

# 重複組み合わせ列挙
all = itertools.combinations_with_replacement([1, 2, 3], 2)