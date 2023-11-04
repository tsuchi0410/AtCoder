rule = list(map(int,input().split()))

koma = list(map(int,input().split()))
move = list(map(int,input().split()))


masu = [0] * rule[0]

for a in koma:
    masu[a - 1] = 1

cnt = 0
cur = 0
for a in move:
    cur = 0
    cnt = 0
    for b in masu: 
        cur += 1
        if b == 1:
            cnt += 1
        if a == cnt and cur < rule[0]:
            if masu[cur] == 0:
                masu[cur - 1] = 0
                masu[cur] = 1

cnt = 0
r = []
for i in range(len(masu)):
    cnt += 1
    if masu[i] == 1:
        r.append(cnt)


print(*r)






