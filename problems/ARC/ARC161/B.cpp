#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for(int i = a; i < b; i++)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define fore(i, a) for(auto &i : a)

#define all(x) (x).begin(),(x).end()

int main(){
    vector<ll> v;
    rep(i, 0, 60){
        rep(j, i+1, 60){
            rep(k, j+1, 60){
                ll num = (ll)pow(2, i) + (ll)pow(2, j) + (ll)pow(2, k);
                v.push_back(num);
            }
        }
    }
    sort(all(v));
    int T;
    cin >> T;
    rep(_, 0, T){
        ll N;
        cin >> N;
        auto itr = upper_bound(all(v), N);
        if (itr == v.begin()) cout << -1 << endl;
        else cout << *prev(itr) << endl;
    }
    
}