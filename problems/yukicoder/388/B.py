S = input()
str = "yukicoder"
l = 0
r = 9
ans = 0
cnt = 0
while r < len(S) + 1:
    if S[l:r] == str:
        l += 9
        r += 9
        cnt += 1
    else:
        cnt = 0
        l += 1
        r += 1
    ans = max(ans, cnt)
print(ans)