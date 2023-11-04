#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for(int i = a; i < b; i++)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define fore(i, a) for(auto &i : a)

#define all(x) (x).begin(),(x).end()

template <typename T>
int bisect_left(vector<T> &X, T v){
    return lower_bound(X.begin(), X.end(), v) - X.begin();
}
template <typename T>
int bisect_right(vector<T> &X, T v){
    return upper_bound(X.begin(), X.end(), v) - X.begin();
}

int main(){
    ll N, K;
    cin >> N >> K;
    map<ll, ll> mp;
    rep(i, 0, N){
        ll a, b;
        cin >> a >> b;
        mp[a] += b;
    }
    fore(i, mp){
        auto k = i.first;
        auto v = i.second;
        K -= v;
        if(K <= 0){
            cout << k << endl;
            return 0;
        }
    }
}