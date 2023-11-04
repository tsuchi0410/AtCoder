import math
T = int(input())

for i in range(T):
    N, D, K = (int(x) for x in input().split())
    K -= 1
    
    g = math.gcd(N, D)

    # 周期
    loop = N // g

    ii = K // loop
    cnt = K % loop
    
    print(D * cnt % N + ii)