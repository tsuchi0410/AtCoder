from collections import deque
n = int(input())
s = input()

q = deque([n])
for i in range(n-1, -1, -1):

    if s[i] == 'R':
        q.appendleft(i)
    else:
        q.append(i)

print(*q)