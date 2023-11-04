import math
n, a, b = (int(x) for x in input().split())

if math.gcd(a, b) == 1:

    cnt_a = n // a
    cnt_b = n // b
    cnt_ab = n // (a*b)

    s = n * (n+1) // 2

    if a <= n:
        syokou = a
        mod = n % a
        makkou = n - mod
        sa = (syokou + makkou) * cnt_a // 2
    else:
        sa = 0

    if b <= n:
        syokou = b
        mod = n % b
        makkou = n - mod
        sb = (syokou + makkou) * cnt_b // 2
    else:
        sb = 0

    if a*b <= n:
        syokou = a*b
        mod = n % (a*b)
        makkou = n - mod
        sab = (syokou + makkou) * cnt_ab // 2
    else:
        sab = 0

    print(s - ((sa+sb) - sab))

else:

    c = min(a, b)
    cnt_c = n // c
    cnt_ab = n // math.gcd(a,b)

    s = n * (n+1) // 2
    
    if c <= n:
        syokou = c
        mod = n % (c)
        makkou = n - mod
        sc = (syokou + makkou) * cnt_c // 2
    else:
        sc = 0
        
    if  <= n:
        syokou = c
        mod = n % (c)
        makkou = n - mod
        sc = (syokou + makkou) * cnt_c // 2
    else:
        sc = 0

    print(s - sc)