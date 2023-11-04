#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for(int i = a; i < b; i++)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define fore(i, a) for(auto &i : a)

#define all(x) (x).begin(),(x).end()

int main(){
    ll N, K;
    cin >> N >> K;
    vector<ll> x(N);
    rep(i, 0, N){
        cin >> x[i];
    }
    ll ans = 1 << 30;
    if(K == 1){
        rep(i, 0, N){
            ans = min(ans, abs(x[i]))
        }
    } else{
        vector<ll> s(n)
        int l = 0;
        ll a = 0;
        for(int r = 1; r < N; r++){
            a += 
        }
    }

    
}