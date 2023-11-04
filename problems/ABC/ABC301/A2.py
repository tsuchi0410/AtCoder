N = int(input())
S = input()
if S.count("T") == S.count("A"):
    print("T") if S[-1] == "A" else print("A")
else:
    print("T") if S.count("T") > S.count("A") else print("A")