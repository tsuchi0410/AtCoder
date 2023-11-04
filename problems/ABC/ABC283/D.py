from collections import deque
q = deque([])
s = input()
d = {}
for i in range(len(s)):
    if s[i] == '(':
        q.append(i)
    elif s[i] == ')':
        # '('のidx
        idx = q.pop()
        new_d = {}
        for i in d:
            if d[i] < idx:
                new_d[i] = d[i]
        d = new_d
    else:
        if s[i] in d:
            print('No')
            exit()
        else:
            d[s[i]] = i

print('Yes')