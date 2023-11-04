s = input()
t = input()

if len(t) > len(s):
    print('No')
    exit()
elif s == t:
    print('Yes')
else:
    for i in range(len(s)+1-len(t)):
        if s[i:i+len(t)] == t:
            print('Yes')
            exit()  
    print('No')