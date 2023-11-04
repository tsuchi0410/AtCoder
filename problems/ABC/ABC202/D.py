"""
先頭から順に決めていく
"a" と決めるとすると残りのグループ数（組み合わせ）は C(A-1+B, B)
"""

import math
A, B, K = map(int,input().split())
S = ""
while True:
    if K > math.comb(A - 1 + B, B):
        K -= math.comb(A - 1 + B, B)
        S += "b"
        B -= 1
    else:
        S += "a"
        A -= 1

    if A - 1 + B < 0:
        break

print(S)
