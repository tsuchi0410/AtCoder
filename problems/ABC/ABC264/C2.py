H1,W1 = (int(x) for x in input().split())
A = []  
for i in range(H1):
    A.append(list(map(int,input().split())))
H2,W2 = (int(x) for x in input().split())
B = []
for i in range(H2):
    B.append(list(map(int,input().split())))
    
# col
for i in range(1 << H1):
    # row
    for j in range(1 << W1):
        li1 = []
        
        for k in range(H1):
            li2 = []
            for l in range(W1):
                
                if (i >> k) & 1 == 1 and (j >> l) & 1 == 1:
                    li2.append(A[k][l])
                    
            if len(li2) > 0:
                li1.append(li2)
            
        # ans
        if li1 == B:
            print('Yes')
            exit()
            
        # print(li1)
            
print('No')        
                    
                