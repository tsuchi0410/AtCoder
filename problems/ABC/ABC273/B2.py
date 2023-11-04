from decimal import Decimal, ROUND_HALF_UP
x, k = (int(x) for x in input().split())
x = str(x)
for i in range(k+1):
    
    if i == 0:
        x = Decimal(x).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    else:
        a = str()
        a = '1E' + str(i)
        x = Decimal(x).quantize(Decimal(a), rounding=ROUND_HALF_UP)
print(int(x))

