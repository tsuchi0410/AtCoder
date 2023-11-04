N = int(input())
A = []
B = []

time = 0
for i in range(N):
    x,y = (int(x) for x in input().split())
    A.append(x)
    B.append(y)
    time += x/y

# print(time)

ans = 0
timecnt = 0
for i in range(N):
    if timecnt + (A[i]/B[i]) <= time/2:
        timecnt += A[i]/B[i]
        ans += A[i]
    else:
        ans += B[i]*(time/2-timecnt)
        break

print(ans)


     
