h, w = (int(x) for x in input().split())
a = []
b = []
for i in range(h):
    a.append(list(map(int,input().split())))
    b.append([0] * w)

sum_col = []
for i in range(h):
    sum_col.append(sum(a[i]))

tr = []
for i in range(w):
    tr_row = []
    for vector in a:
        tr_row.append(vector[i])
    tr.append(tr_row)    

sum_row = []
for i in range(w):
    sum_row.append(sum(tr[i]))
    
for i in range(h):
    for j in range(w):
        
        b[i][j] = sum_col[i] + sum_row[j] - a[i][j]

for i in b:
    print(*i, sep = ' ')