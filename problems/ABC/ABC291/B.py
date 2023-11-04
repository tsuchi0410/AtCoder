N = int(input())
X = list(map(int,input().split()))
X.sort()

X = X[N:]
X.sort(reverse = True)
X = X[N:]

ans = 0
for i in range(len(X)):
    ans += X[i]

print(ans / len(X))
