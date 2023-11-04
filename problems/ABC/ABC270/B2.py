x, y, z, = (int(x) for x in input().split())

if y < 0:
    x *= -1
    y *= -1
    z *= -1
    
if x < y:
    print(abs(x))

else:
    if z < y:
        print(abs(z) + abs(x - z))
    else:
        print('-1')