a, b = (int(x) for x in input().split())
import math

# 二分探索
def nibutan():
    
    
    l = 0
    r = a # 任意
    ans = float('inf')
    idx = 0
    c = (r + l) // 2
    while(1 < r - l):
        # res = b * (c - 1) + a / (math.sqrt(c))
        res_left = b * (c - l - 1) + a / (math.sqrt(c - l))
        res_right = b * (r - c - 1) + a / (math.sqrt(r - c))
        
        if res_left < res_right:
            r = c
        else:
            l = c
        
        if ans > res_left:
            ans = res_left
            idx = c - l
        elif ans > res_right:
            ans = res_right
            idx = r - c
    
    print(idx)
    return ans

res = nibutan()
print(res)

