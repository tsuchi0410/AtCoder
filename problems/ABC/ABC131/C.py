import math
A, B, C, D = map(int,input().split())
CD = C * D // math.gcd(C, D)
cnt1 = (A - 1) // C
cnt2 = (A - 1) // D
cnt3 = (A - 1) // CD
ans1 = cnt1 + cnt2 - cnt3
cnt4 = B // C
cnt5 = B // D
cnt6 = B // CD
ans2 = cnt4 + cnt5 - cnt6
print(B - A + 1 - (ans2 - ans1))