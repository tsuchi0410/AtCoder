N, K = map(int, input().split())
event = []
cnt = 0
for i in range(N):
    a, b = (int(x) for x in input().split())   
    event.append([a, b])
    cnt += b

if cnt <= K:
    print(1)
    exit()

event.sort()
for day, b in event:
    cnt -= b
    if cnt <= K:
        print(day + 1)
        exit()
    