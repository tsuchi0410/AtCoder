#include <bits/stdc++.h>
using namespace std;
int main(){
    int H, W, ans;
    cin >> H >> W;
    if(H == 1 || W == 1) ans = H * W;
    else ans = ((H + 1) / 2) * ((W + 1) / 2);
    cout << ans << endl;
}

