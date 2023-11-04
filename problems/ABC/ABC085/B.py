N = int(input())

d = []

for i in range(N):
    d.append(int(input()))

d2 = sorted(d, reverse = True)

c = 1
for i in range(N):
    if i == N-1:
        break
    if not d2[i] == d2[i+1]:
        c += 1
    
print(c)
