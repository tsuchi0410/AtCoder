s = input()
k = int(input())

l = [0]
for i in range(0, len(s)):
    if s[i] == 'X':
        l.append(l[i] + 1)
    else:
        l.append(l[i])

cnt = 0
ans = 0
le = 0; ri = 0
while True:
    if l[ri] < l[ri+1]:
        ri += 1
        cnt += 1
    else:
        if k > 0:
            k -= 1
            cnt += 1
            ri += 1
        else:
            if l[le] < l[le+1]:
                cnt -= 1
                le += 1
            else:
                cnt -= 1
                le += 1
                k += 1
    ans = max(ans, cnt)
    if ri == len(l) - 1:
        break

print(ans)