n, q = (int(x) for x in input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
st = []
for i in range(q):
    st.append(list(map(int,input().split())))
    
for i in range(q):
    idx = st[i][0] - 1
    num = st[i][1] 
    print(a[idx][num])