S = str(input())

n = len(S)
cnt = n
while (1):
    
    if S[cnt-5:cnt] == 'dream':
        cnt -= 5
    elif S[cnt-7:cnt] == 'dreamer':
        cnt -= 7
    elif S[cnt-5:cnt] == 'erase':
        cnt -= 5
    elif S[cnt-6:cnt] == 'eraser':
        cnt -= 6
    else:
        print('NO')
        exit()
        
    
    
    if cnt == 0:
        print('YES')
        exit()