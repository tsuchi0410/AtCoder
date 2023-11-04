def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


N = int(input())
l = primes(20 ** 5)

cnt = 0
for i in range(len(l)):
    if l[i]**2 > N:
        break
    for j in range(i+1,len(l)):
        if l[i] ** 2 * l[j] > N:
            break
        for k in range(j+1,len(l)):
            if l[i]**2 * l[j] * l[k]**2 <= N:
                cnt += 1
            else:
                break

print(cnt)