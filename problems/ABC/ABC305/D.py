import bisect
N=int(input())
A=list(map(int,input().split()))
A2=[]
A3=[]
for i in range(N):
    if i % 2 != 0:
        A2.append(A[i]-A[i-1])
        A3.append(0)
    else:
        A2.append(0)
        A3.append(A[i]-A[i-1])

A3[0] = 0

S1=[0]
S2=[0]
for i in range(N):
    S1.append(S1[i]+A2[i])
    S2.append(S2[i]+A3[i])

S1 = S1[1:]
S2 = S2[1:]

Q = int(input())
for _ in range(Q):
    l,r=map(int,input().split())
    idx_l=bisect.bisect_left(A, l)
    idx_r=bisect.bisect_left(A, r)
    if idx_l==idx_r:
        if idx_l % 2 == 0:
            print(r-l)
        else:
            print(0)
    else:
        cnt=0
        if idx_l % 2 == 0:
            cnt+=A[idx_l]-l
        if idx_r % 2 == 0:
            cnt+=r-A[idx_r-1]
        cnt+=S2[idx_r-1]-S2[idx_l]
        print(cnt)