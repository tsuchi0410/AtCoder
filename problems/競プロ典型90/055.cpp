#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for(int i = a; i < b; i++)

int main(){
    ll N, P, Q;
    cin >> N >> P >> Q;
    vector<ll> A(N);
    rep(i, 0, N) cin >> A.at(i);

    ll ans = 0;
    rep(i, 0, N){
        ll num;
        num = A.at(i) % P;
        rep(j, i + 1, N){
            num *= A.at(j) % P;
            rep(k, j + 1, N){
                num *= A.at(k) % P;
                rep(l, k + 1, N){
                    num *= A.at(l) % P;
                    rep(m, l + 1, N){
                        num *= A.at(m) % P;
                        if(num % P == Q) ans++;
                       

                    }
                }
            }
        }
    }
    cout << ans << endl;

}