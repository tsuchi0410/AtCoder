t = int(input())

# N = p^2 * q
for i in range(t):
    n = int(input())
    
    for j in range(2, 10**7):
        if n % j**2 == 0:
            print(j, n // j**2)
            break
        elif n % j == 0:
            print(int((n // j)**0.5), j)
            break