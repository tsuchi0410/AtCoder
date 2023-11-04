X = int(input())
S = [0]
num = str(X)
for i in range(len(num)):
    S.append(S[i] + int(num[i]))

ans = []
for i in range(len(num), -1, -1):
    y = S[i]
    if y < 10:
        ans.append(str(y))
    else:
        ans.append(str(y % 10))
        S[i - 1] += S[i] // 10

ans.reverse()
ans = "".join(ans)
if ans[0] == "0":
    print(ans[1:])
else:
    print(ans)
