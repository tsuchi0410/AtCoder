n=int(input())
a=list(map(int,input().split()))
Q=int(input())
for i in range(Q):
    q=list(map(int,input().split()))
    if q[0] == 1:
        a[q[1]-1] = q[2]
    else:
        print(a[q[1]-1])