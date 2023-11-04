N = int(input())
l = 1
r = N
while True:
    mid = (l + r) // 2
    print("?", mid)
    res = int(input())
    if res == 0:
        l = mid
    else:
        r = mid
    if abs(l - r) == 1:
        print("!", l)
        exit()