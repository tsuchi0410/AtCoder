S = []
for i in range(10):
    S.append(input())
    
for i in range(10):
    
    for j in range(10):
        
        if S[i][j] == '#':
            a = i
            c = j

            for k in range(9,-1,-1):
                
                if S[i][k] == '#':
                    d = k
                    
                    for i in range(9, -1, -1):
    
                        for j in range(10):
        
                            if S[i][j] == '#':
                                b = i
                                print(a+1, b+1)
                                print(c+1, d+1)
                                exit()
            
    
    
    


