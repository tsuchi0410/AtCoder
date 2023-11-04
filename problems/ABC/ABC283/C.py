s=input()
ans = 0
i = 0
while i < len(s):
    if s[i] == '0':
        if i+1 < len(s):
            if s[i+1] == '0':
                ans += 1
                i += 1
            else:
                ans += 1
        else:
            ans += 1
    else:
        ans += 1
    i += 1

print(ans)