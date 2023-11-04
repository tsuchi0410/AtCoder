S = input()
ans = 0
for c in S:
    if c == 'A':
        ans += 1
    else:
        ans = ans*2

print(ans)