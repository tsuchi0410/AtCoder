S = list(map(int, input().split()))

S2 = sorted(S)
if S == S2:
    for i in S:
        if not 100 <= i <= 675:
            print("No")
            exit()
        if not i % 25 == 0:
            print("No")
            exit()
    print("Yes")
    exit()
else:
    print("No")
    exit() 