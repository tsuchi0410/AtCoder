N,A,B=map(int,input().split())
C = list(map(int,input().split()))

num = A+B
for i in range(N):
    if C[i] == num:
        print(i+1)
        exit()