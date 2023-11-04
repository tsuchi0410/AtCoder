X, K, D = (int(x) for x in input().split())

if X // D < K:
    c = K - X // D
    
    if X < 0:
        c -= 1
    
    if c % 2 == 0:
        print(X % D)
    else:
        print(abs(X % D - D))    
else:
    print(min(abs(X - K * D), abs(X + K * D)))