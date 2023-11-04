x,y,a,b = (int(x) for x in input().split())

cnt = 0
while True:
    if x * a > y:
        break
    else:
        if x * a - x < b:
            x *= a
            cnt += 1
        else:
            break

cnt2 = ((y - 1) - x) // b
print(cnt+cnt2)