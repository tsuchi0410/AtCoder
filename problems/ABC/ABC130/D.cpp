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
    vector<ll> a(N);
    rep(i, 0, N){
        cin >> a[i];
    }
    vector<ll> s;
    s.push_back(0);
    rep(i, 0, N){
        s.push_back(s[i] + a[i]);
    }
    ll ans = 0;
    rep(i, 0, N + 1){
        int il = bisect_left(s, 1ll * (s[i] + K));
        // cout << il << endl;
        if(i != il){
            ans += N + 1 - il;
        }
    }
    cout << ans << endl;
}