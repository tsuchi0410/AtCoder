N = 30

# read
ball = []
dic = {}
for i in range(N):
    b = list(map(int, input().split()))
    ball.append(b)
    for j in range(len(b)):
        dic[b[j]] = [i, j]
    


