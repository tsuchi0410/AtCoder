from collections import deque
n, x = (int(x) for x in input().split())
s = str(input())

s = list(s)
q = deque(s)
new_q = deque()
for i in range(n):
    y = q.popleft()
    if y != 'U':
        new_q.append(y)
    else:
        if len(new_q) == 0:
            new_q.append(y)
        else:
            if y == 'U' and new_q[0] != 'U':
                new_q.pop()
            else:
                new_q.append(y)
                
            
            

for i in range(len(new_q)):
    y = new_q.popleft()
    if y == 'U':
        x //= 2
    elif y == 'L':
        x *= 2
    else:
        x = x * 2 + 1

print(x)
