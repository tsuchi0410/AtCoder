from decimal import Decimal, ROUND_HALF_UP

def round_to(x, num):
    """
    一の位を四捨五入 : -1
    小数第一位を四捨五入(整数) : 0
    小数第二位を四捨五入 : 1
    """
    x = str(x)
    if num == 0:
        return Decimal(x).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    elif num < 0:
        num *= -1
        s = '1E' + str(num)
        return Decimal(x).quantize(Decimal(s), rounding=ROUND_HALF_UP)
    elif num > 0:
        s = str(1 / 10 ** num) 
        return Decimal(x).quantize(Decimal(s), rounding=ROUND_HALF_UP)


from decimal import Decimal, ROUND_HALF_UP
x = input()
x = str(x)
# 小数点第一位を四捨五入
res = Decimal(x).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
# 小数点を四捨五入
res = Decimal(x).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
print(float(res))

# 1の位で四捨五入
res = Decimal(x).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)
# 10の位で四捨五入
res = Decimal(x).quantize(Decimal('1E2'), rounding=ROUND_HALF_UP)
print(int(res))