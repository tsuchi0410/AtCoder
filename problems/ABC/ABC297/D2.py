def gcd(a, b):
    cnt = 0
    while b:
        cnt += a // b
        a, b = b, a % b
    return cnt

A, B = map(int, input().split())
print(gcd(A, B) - 1)
