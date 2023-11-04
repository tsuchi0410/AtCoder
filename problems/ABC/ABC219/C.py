X = input()
N = int(input())
S = []
for i in range(N):
    S.append(input())

new_d = {}
for i in range(len(X)):
    new_d[X[i]] = i

# print(new_d)

l = []
buf = []
for i in range(N):
    for j in range(len(S[i])):
        if S[i][j] in new_d:
            buf.append(new_d[S[i][j]])

    l.append([buf,S[i]])
    buf = []

l = sorted(l)

for i in range(N):
    print(l[i][1])   



