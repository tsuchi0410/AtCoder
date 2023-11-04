N = int(input())
A = list(map(int,input().split()))
A.sort()
B = A[N//2+1:]
A = A[:N//2+1]
i = 0
j = 0
while j < len(B):
    if A[i] < B[j] and A[i + 1] < B[j]:
        i += 1
        j += 1
    else:
        print("No")
        exit()
print("Yes")