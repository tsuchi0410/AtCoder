n,k=(int(x) for x in input().split())
a=list(map(int,input().split()))

if k > n:
    ave = [k//n] * n
    for i in range(k%n):
        ave[i] += 1
elif k == n:
    ave = [1] * n
else:
    ave = [0] * n
    for i in range(k):
        ave[i] += 1

cnt = 0
st = []
for i in range(n):
    if ave[i] > a[i]:
        cnt += ave[i] - a[i]
        st.append(a[i] - ave[i])
    elif a[i] > ave[i]:
        st.append(a[i] - ave[i])
    else:
        st.append(0)

ans = []
for i in range(n):
    if st[i] < 0:
        ans.append(0)
    else:
        if st[i] >= cnt:
            ans.append(st[i] - cnt)
        else:
            ans.append(0)
            cnt -= st[i]

print(*ans)