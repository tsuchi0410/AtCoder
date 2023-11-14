# 正確な浮動小数点の計算を行う
from decimal import Decimal
A, B = map(Decimal, input().split())
print(A * B)