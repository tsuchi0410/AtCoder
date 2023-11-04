import bisect
S = input()

r = []
l = []

for i in range(len(S)):
    if S[i] == "R":
        r.append(i)
    else:
        l.append(i)

ans = [0] * len(S)
for i in range(len(S)):
    if S[i] == "R":
        idx = bisect.bisect_left(l, i)
        diff = l[idx] - i
        if diff % 2 == 0:
            ans[l[idx]] += 1
        else:
            ans[l[idx] - 1] += 1
    else:
        idx = bisect.bisect_left(r, i)
        diff = i - r[idx - 1]
        if diff % 2 == 0:
            ans[r[idx - 1]] += 1
        else:
            ans[r[idx - 1] + 1] += 1

print(*ans)