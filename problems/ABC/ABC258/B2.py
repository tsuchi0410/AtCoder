N = int(input())

A = []
for i in range(N):
    buf = int(input())
    A.append(buf)

vec = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,1],[-1,1],[1,-1]]

cur = []
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(len(vec)):
            for l in range(N):
                x = i + vec[k][0]*l
                y = j + vec[k][1]*l
                if x >= N:
                    x = x - N
                if y >= N:
                    y = y - N

                buf = str(A[x])[y]
                cur.append(buf)
            
            res = int("".join(cur))
            ans = max(ans, res)
            
            cur = []

print(ans)
            