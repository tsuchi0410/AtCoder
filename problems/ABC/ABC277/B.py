n = int(input())
s = []
for i in range(n):
    s.append(input())

s = list(set(s))
if len(s) == n:
    pass
else:
    print('No')
    exit()
for i in range(len(s)):
    if s[i][0] == 'H' or s[i][0] == 'D' or s[i][0] == 'C'or s[i][0] == 'S':
        pass
    else:
        print('No')
        exit()

l = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
for j in range(len(s)):
    if s[i][1] in l:
        pass
    else:
        print('No')
        exit()
        
print('Yes')