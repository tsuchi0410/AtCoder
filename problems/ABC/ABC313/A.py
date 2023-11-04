N = int(input())
P = list(map(int, input().split()))
x = P[0]

if max(P) == x:
    if P.count(x) == 1:
        print(0)
    else:
        print(1)
    
else:
    print(max(P) - x + 1)