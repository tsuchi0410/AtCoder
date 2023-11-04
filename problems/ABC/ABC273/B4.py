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

X, K = map(int, input().split())
for i in range(K + 1):
    X = round_to(X, -i)
print(int(X))