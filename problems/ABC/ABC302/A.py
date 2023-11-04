A, B = map(int,input().split())
if A % B > 0:
    print(A // B + 1)
else:
    print(A // B)