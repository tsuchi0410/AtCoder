def isprime(N):
    if N < 2:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True

Q = int(input())
for _ in range(Q):
    X = int(input())
    if isprime(X):
        print("Yes")
    else:
        print("No")