N = int(input())
A = list(map(int,input().split()))
l = []
D = int(input())
for i in range(D):
    L, R = map(int, input().split())
    L -= 2
    l.append([L, R])

left = [A[0]]
for i in range(1, N):
    left.append(max(left[-1], A[i]))

A.reverse()
right = [A[0]]
for i in range(1, N):
    right.append(max(right[-1], A[i]))

right.reverse()
for i in range(D):
    print(max(left[l[i][0]], right[l[i][1]]))

