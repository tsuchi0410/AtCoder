S = input()


if S[0] == '1':
    print('No')
    exit()

l = ['1', '1', '1', '1', '1', '1', '1']

if S[0] == '0' and S[4] == '0':
    l[3] = '0'

if S[1] == '0' and S[7] == '0':
    l[2] = '0'

if S[8] == '0' and S[2] == '0':
    l[4] = '0'
    
if S[3] == '0':
    l[1] = '0'

if S[5] == '0':
    l[5] = '0'

if S[6] == '0':
    l[0] = '0'

if S[9] == '0':
    l[6] = '0'
    
    
f = 0
for i in range(len(l)):
    if l[i] == '1':
        
        if i+1 < len(l):
            for j in range(i+1, len(l)):
                if l[j] == '0':
                    
                    if j+1 < len(l):
                        for k in range(j+1, len(l)):
                            if l[k] == '1':
                                print('Yes')
                                exit()
                        
print('No')                
