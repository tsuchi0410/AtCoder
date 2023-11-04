N = int(input())
S = input()

ans = 0
i = 0
cnt = 0
j = 0
f = True
while f == True:
    if i >= N:
        break
    if S[i] == "o":
        cnt = 0
        j = i
        while True:
            if j >= N:
                f = False
                break
            if S[j] == "o":
                cnt += 1
                j += 1
            else:
                ans = max(ans, cnt)
                break
        i = j
    else:
        i += 1

S = S[::-1]
i = 0
cnt = 0
j = 0
f = True
while f == True:
    if i >= N:
        break
    if S[i] == "o":
        cnt = 0
        j = i
        while True:
            if j >= N:
                f = False
                break
            if S[j] == "o":
                cnt += 1
                j += 1
            else:
                ans = max(ans, cnt)
                break
        i = j
    else:
        i += 1


if ans == 0:
    print(-1)
else:
    print(ans)