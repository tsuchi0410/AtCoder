n = int(input())
s = input()

f = 0
cnt = 0
ans = []
for i in range(n):
    if s[i] == '"':
        if cnt % 2 == 0:
            f = 1
        else:
            f = 0
        cnt += 1

        ans.append(s[i])
        continue

    if f == 0:
        if s[i] == ',':
            ans.append('.')
        else:
            ans.append(s[i])
    else:
        ans.append(s[i])

print(''.join(ans))
