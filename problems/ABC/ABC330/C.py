# int main(){
#   LL(D);
#   ll nmax = 10000000;
#   ll ans = INF;
#   rep(i, nmax){
#     ll x = i * i;
#     if(D < x){
#       break;
#     }
#     ll y = sqrt(D - x);
#     chmin(ans, abs(x + y * y - D));
#     // debug(x, y, ans)
#   }
#   print(ans);
# }

import math
D = int(input())
ans = float("inf")
for i in range(10**7):
    x = i * i
    n1 = D - x
    print(n1)
    y = int(math.sqrt(n1))
    ans = min(ans, abs(x + y * y - D))
    y += 1
    ans = min(ans, abs(x + y * y - D))
print(ans)
