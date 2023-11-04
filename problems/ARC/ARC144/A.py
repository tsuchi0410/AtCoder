N = int(input())
M = 2 * N

L = []
if N % 4 == 0:
    print(M)
    print("4" * (N // 4))
else:
    print(M)
    print(str(N % 4) + "4" * (N // 4))