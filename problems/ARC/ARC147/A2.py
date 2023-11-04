from collections import deque

N =int(input())
A = list(map(int, input().split()))

A = sorted(A)
A = deque(A)
cnt = 0
while(1):
    
    if len(A) == 1:
        print(cnt)
        exit()
    
    res = A[-1] % A[0]
    
    if res == 0:
        A.pop()
    else:
        A.pop()
        A.appendleft(res)
        
    cnt += 1
    
    