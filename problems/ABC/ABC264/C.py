import itertools 
H1,W1 = (int(x) for x in input().split())
A = []
for i in range(H1):
    A.append(list(map(int,input().split())))
H2,W2 = (int(x) for x in input().split())
B = []
for i in range(H2):
    B.append(list(map(int,input().split())))


h = [_ for _ in range(H1)]
w = [_ for _ in range(W1)]

for i in itertools.combinations(h, H2):
    for j in itertools.combinations(w,W2):
        
        # print(i,j)

        li2 = []
        for k in i:
            li = []
            for l in j:

                # print(k,l)
                li.append(A[k][l])
            
            li2.append(li)

        # print(li2)
        if B == li2:
            print("Yes")
            exit()

print("No")