A, B, C, X, Y = (int(x) for x in input().split())

if A + B > 2 * C:
    if X > Y:
        Csum = C * Y * 2
        var1 = min((X - Y) * A, (X - Y) * 2 * C)
        print(Csum+var1)
    else:
        Csum = C * X * 2
        var2 = min((Y - X) * B, (Y - X) * 2 * C)
        print(Csum+var2)
else:
    Asum = X * A
    Bsum = Y * B
    print(Asum+Bsum)
