T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    f = False
    for i in range(1, N):
        s1 = S[:i]
        s2 = S[i:]
        if s1 < s2:
            f = True
            break
    if f == True:
        print("Yes")
    else:
        print("No")