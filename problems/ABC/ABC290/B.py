N, K = (int(x) for x in input().split())
S = input()

ans = []
for i in range(N):
    if K == 0:
        ans.append("x")
    elif S[i] == "o":
        ans.append("o")
        K -= 1
    elif S[i] == "x":
        ans.append("x")

print("".join(ans))