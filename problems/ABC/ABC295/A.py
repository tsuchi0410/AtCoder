N = int(input())
W = list(map(str, input().split()))
S = {"and", "not", "that", "the", "you"}
for i in W:
    if i in S:
        print("Yes")
        exit()
print("No")