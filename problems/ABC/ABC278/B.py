h, m = (str(x) for x in input().split())

if len(h) == 1:
    h = '0' + h
if len(m) == 1:
    m = '0' + m

while(1):
    h = str(h)
    m = str(m)
    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    if int(h[1]) <= 5:
        if int(h[0]) < 2:
            print(int(h),int(m))
            exit()
        elif int(m[0]) < 4:
            print(int(h),int(m))
            exit()
    h = int(h)
    m = int(m)
    m += 1
    if m == 60:
        h += 1
        m = '00'
    if h == 24:
        h = '00'
        m = '00'