a, b = (int(x) for x in input().split())
if b == a*2 or b == a*2+1:
    print('Yes')
else:
    print("No")