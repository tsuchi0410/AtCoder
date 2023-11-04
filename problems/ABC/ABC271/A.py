n = int(input())
n2 = format(n, 'x')
if len(n2) == 1:
    print('0' + n2.upper())
else:
    print(n2.upper())