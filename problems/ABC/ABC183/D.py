N, W = map(int,input().split())
D = 2*10**5+10
l = [0] * D
for i in range(N):
    S, T, P = map(int,input().split())
    
    # 区間にvを加算
    l[S] += P
    l[T] -= P

# 累積和
s = [0]
for i in range(D):
    s.append(s[i] + l[i])

if max(s) <= W:
    print("Yes")
else:
    print("No")