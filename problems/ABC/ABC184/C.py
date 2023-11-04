from collections import deque
n = 12

r1, c1 = (int(x) for x in input().split())
x, y = (int(x) for x in input().split())

a, b = r1, c1
c, d = x, y

if a == c and b == d:
    print('0')
    exit()

x -= r1
y -= c1

if x < 0:
    x *= -1
if y < 0:
    y *= -1

if x > 5 or y > 5:
    
    if x == y:
        print('1')
        exit()
        
    if y > x:
        a = x
        b = y
        c = x + (b - a) // 2
        
        if abs(x - c) == abs(y - c):
            print('2')
        else:
            print('3')
            
    else:
        if x == y:
            print('1')
            exit()
            
        a = y
        b = x
        c = y + (b - a) // 2
        
        if abs(x - c) == abs(y - c):
            print('2')
        else:
            print('3')
        
else:
    if a + b == c + d or a - b == c - d or abs(a - c) + abs(b - d) <= 3:
        print('1')
    else:
        print('2')