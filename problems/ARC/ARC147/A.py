import heapq

N =int(input())
A = list(map(int, input().split()))

heapq.heapify(A)
B = [-A[i] for i in range(len(A))]
heapq.heapify(B) 

cnt = 0
while(1):

    if len(B) == 1:
        print(cnt)
        exit()
        
    res = B[0]*(-1) % A[0]
    
    if res == 0:
        heapq.heappop(B)
    else:
        heapq.heappop(B)
        heapq.heappush(B, -1 * res)
        heapq.heappush(A, 1 * res)

    cnt += 1
