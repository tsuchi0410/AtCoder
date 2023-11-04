x, y, z, = (int(x) for x in input().split())

if y < 0 and 0 < x:
    print(abs(x))
    exit()

if y > 0 and 0 > x:
    print(abs(x))
    exit()

if 0 < y and y > x:
    print(abs(x))
    exit()

if y < 0 and x > y:
    print(abs(x))
    exit()

if 0 < y and y < x:
    if z < y:
        print(abs(z) + abs(x - z))
    else:
        print('-1')

if y < 0 and x < y:
    if y < z:
        print(abs(z) + abs(x - z))
    else:
        print('-1')

