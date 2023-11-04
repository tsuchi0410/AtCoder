s = input()
ans = 0
for i in range(len(s)):
    ans += 26 ** (len(s)-(i+1)) * (ord(s[i])-64)
print(ans)