from collections import deque
q = int(input())

deq = deque([])
for i in range(q):
    
    que = list(map(int,input().split()))

    if que[0] == 1:
        x = que[1]
        c = que[2]
        
        a = [x, c]
        deq.append(a)
    
    if que[0] == 2:
        ball = que[1]
        sum = 0
        
        while (1):
            a = deq.popleft()
            
            if ball < a[1]:
                print(sum + a[0] * ball)
                a = [a[0], a[1] - ball]
                deq.appendleft(a)
                break
            
            if ball == a[1]:
                print(sum + a[0] * ball)
                break
            
            else:
                sum += a[0] * a[1]
                ball -= a[1]
                
        


