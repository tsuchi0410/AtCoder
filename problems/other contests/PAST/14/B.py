from decimal import Decimal, getcontext
D = int(input())
getcontext().prec = D
A = Decimal(input())
B = Decimal(input())
num = A + B
num = int(num)
if num == 0:
    print(A + B)
else:
    num = str(num)
    getcontext().prec = D + len(num)
    print(A + B)