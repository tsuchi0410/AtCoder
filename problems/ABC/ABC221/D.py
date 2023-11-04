N = int(input())
event = []
for i in range(N):
    A, B = list(map(int,input().split()))
    event.append([A, True])
    event.append([A + B, False])

event.sort()
login_cnt = 0
pre_day = 0
ans = [0] * (N + 1)
for i in range(len(event)):
    day = event[i][0]
    flag = event[i][1]
    
    if i == 0:
        pre_day = day
        login_cnt += 1
    else:
        time = day - pre_day
        if flag == True:
            ans[login_cnt] += time
            login_cnt += 1
        else:
            ans[login_cnt] += time
            login_cnt -= 1
        pre_day = day

ans = ans[1:]
print(*ans, sep = " ")