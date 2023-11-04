N = int(input())
S = str(input())
W = list(map(int,input().split()))

#子供の人数
child = 0
for i in S:
    if i == '0':
        child += 1

child = int(child)

cnt = [0] * N
count = 0
count2 = 0
count3 = []

for X in range(0, 10**3):
    for i in W:
    # 子供と判定するとき
        if X - i < 0:
            cnt[count] = 0
        else:
            cnt[count] = 1
        count += 1
    
    for j in range(N):
        count2 = abs(cnt[j] - int(S[j]))

    count3.append(abs(N-count2))
    cnt = [0] * N
    count = 0
    count2 = 0


print(min(count3))


