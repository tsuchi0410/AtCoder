import heapq
n = int(input())
tkl = []
for i in range(n):
    tkl.append(list(map(int,input().split())))

q = [-1*(n-1)]
heapq.heapify(q)  
l = [0] * n 
l[-1] = 1

while q:

    w = -1 * heapq.heappop(q)   
    
    for j in range(tkl[w][1]):
        
        if l[tkl[w][j+2] - 1] == 0:
            heapq.heappush(q, -1 * (tkl[w][j+2] - 1))   
            l[tkl[w][j+2] - 1] = 1
    
    
a = 0
for i in range(n):
    if l[i] == 1:
        a += tkl[i][0]
    
print(a)

