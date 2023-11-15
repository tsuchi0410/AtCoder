# 正確な浮動小数点の計算を行う
# CPython で提出！
from decimal import Decimal
A, B = map(Decimal, input().split())
print(A * B)