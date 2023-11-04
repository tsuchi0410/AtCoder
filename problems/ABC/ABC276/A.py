s = input()
for i in range(len(s)-1,-1,-1):
    if s[i] == 'a':
        print(i+1)
        exit()

print('-1')