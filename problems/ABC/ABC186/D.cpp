#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for(int i = a; i < b; i++)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define fore(i, a) for(auto &i : a)

#define all(x) (x).begin(),(x).end()

int main(){
    int N;
    cin >> N;
    vector<ll> v(N);
    rep(i, 0, N){
        cin >> v[i];
    }
    sort(all(v));
    vector<ll> s;
    s.push_back(0);
    rep(i, 0, N){
        s.push_back(s[i] + v[i]);
    }
    ll ans = 0;
    rep(i, 0, N){
        ans += s[N] - s[i + 1] - v[i] * (N - i - 1);
    }
    cout << ans << endl;
}