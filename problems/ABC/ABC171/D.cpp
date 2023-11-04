#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for(int i = a; i < b; i++)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define fore(i, a) for(auto &i : a)

#define all(x) (x).begin(),(x).end()

int main(){
    ll N;
    cin >> N;
    unordered_map<ll, ll> ump;
    rep(i, 0, N){
        ll a;
        cin >> a;
        ump[a]++;
    }
    ll ans = 0;
    fore(p, ump){
        auto k = p.first;
        auto v = p.second;
        ans += k * v;
    }
    ll Q;
    cin >> Q;
    rep(i, 0, Q){
        ll B, C;
        cin >> B >> C;
        if (ump.count(B)){
            ans -= B * ump.at(B);
            ans += C * ump.at(B);
            ump[C] += ump.at(B);
            ump.erase(B);
        }
        cout << ans << endl;
    }
}