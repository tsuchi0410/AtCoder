#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for(int i = a; i < b; i++)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define fore(i, a) for(auto &i : a)

#define all(x) (x).begin(),(x).end()

const int MOD = 1000000007;
long long pow(long long x, long long n) {
    long long ret = 1;
    while (n > 0) {
        if (n & 1) ret = ret * x % MOD;  // n の最下位bitが 1 ならば x^(2^i) をかける
        x = x * x % MOD;
        n >>= 1;  // n を1bit 左にずらす
    }
    return ret;
}

int main(){
    ll N, K;
    cin >> N >> K;
    if (N == 1) cout << K % MOD << endl;
    else if (N == 2) cout << (K * (K - 1)) % MOD << endl;
    else{
        ll ans1 = (K * (K - 1)) % MOD;
        ll cnt = N - 2;
        ll ans2 = pow(K - 2, cnt);
        cout << (ans1 * ans2) % MOD << endl;
    }
}