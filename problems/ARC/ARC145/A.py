N = int(input())
S = str(input())

if N == 2:
    if S == "AB" or S == "BA":
        print("No")
        exit()

if S[0] == "A" and S[N-1] == "B":
    print("No")
    exit()

print("Yes")
