from collections import deque

S = input()
K = int(input())

ans = 0
q = deque()
for right in S:
    
    q.append(right)

    if right == ".":
        if K > 0:
            K -= 1
        else:
            while q:
                left = q.popleft()
                if left == ".":
                    break
    
    ans = max(ans, len(q))

print(ans)
    