N = int(input())
A = list(map(int,input().split()))
ans = sum(A)
B = A[:]
L = A + B
cnt = 0

r = 0
l = 0
tmp = 0
while r < len(L):
    if tmp < N:
        cnt += L[r]
        tmp += 1
    else:
        tmp -= 1
        cnt -= L[l]
        l += 1
    
    if cnt * 10 == ans:
        print("Yes")
        exit()
    elif cnt * 10 > ans:
        while cnt * 10 > ans:
            tmp -= 1
            cnt -= L[l]
            l += 1
    r += 1

print("No")