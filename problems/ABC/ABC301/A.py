N = int(input())
S = input()

if S.count("T") == S.count("A"):
    cnt = S.count("T")
    t = 0
    a = 0
    for i in range(N):
        if S[i] == "T":
            t += 1
        else:
            a += 1
        if t == cnt:
            print("T")
            exit()
        if a == cnt:
            print("A")
            exit()
else:
    if S.count("T") > S.count("A"):
        print("T")
        exit()
    else:
        print("A")
        exit()