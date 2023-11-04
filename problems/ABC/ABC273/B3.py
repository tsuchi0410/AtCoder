from decimal import Decimal, ROUND_HALF_UP
x = input()
x = str(x)
# 小数点第一位を四捨五入
res = Decimal(x).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
# 小数点を四捨五入
# res = Decimal(x).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
# 1の位で四捨五入
# res = Decimal(x).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)
# 10の位で四捨五入
# res = Decimal(x).quantize(Decimal('1E2'), rounding=ROUND_HALF_UP)
print(float(res))