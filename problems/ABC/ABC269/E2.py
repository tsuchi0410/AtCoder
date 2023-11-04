def nibutan_ab(N):
    
    l = a
    r = b
    while(1 < r - l):
        center = (r + l) // 2
        print('?', l+1, r, c+1, d)
        t = int(input())
        if t == N // 2:
            l = center
        else:
            r = center

        N //= 2
    print(l,r)

n = int(input())
a = 0; b = n; c = 0; d = n
x = nibutan_ab(n)

