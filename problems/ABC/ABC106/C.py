s = input()
k = int(input())

c = 0
num = 0
for i in range(len(s)):
    if i == 0 and s[i] == '1':
        for j in range(len(s)):
            if s[j] == '1':
                c += 1
            else:
                num = c 
                break

if k > c:
    print(s[num])
else:
    print('1')