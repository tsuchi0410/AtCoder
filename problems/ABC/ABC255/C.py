X,A,D,N = (int(x) for x in input().split())

if D < 0:
    A = A + D * (N - 1)
    D *= -1
    
def nibutan(X):
    
    l = 0
    r = N
    
    while(1 < r - l):
        center = (r + l) // 2
        
        if X <= A + center * D:
            r = center
        else:
            l = center

    return l, r

if D == 0:
    print(abs(X - A))
    
elif X >= A + N * D:
    print(X - (A + (N - 1) * D))

else:
    res = nibutan(X)
    print(min(abs(X - (A + res[0] * D)), abs(X - (A + res[1] * D))))
