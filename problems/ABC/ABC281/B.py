s = input()

l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l2 = '0123456789'

if len(s) == 8:
    num = ''
    if s[0] in l:
        for i in range(6):
            if s[i+1] not in l2:
                print('No')
                exit()
            else:
                num += s[i+1]
        
        if 100000 <= int(num) <= 999999:
            if s[-1] in l:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')

