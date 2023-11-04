#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define rep(i, a, b) for(int i = a; i < b; i++)
#define rrep(i, a, b) for(int i = a; i >= b; i--)
#define fore(i, a) for(auto &i : a)

#define all(x) (x).begin(),(x).end()

int main(){
    int W, H;
    cin >> W >> H;
    int N;
    cin >> N;
    vector<int> p(N), q(N);
    rep(i, 0, N){
        cin >> p[i] >> q[i];
    }
    int A;
    cin >> A;
    vector<int> a(A);
    rep(i, 0, A){
        cin >> a[i];
    }
    int B;
    cin >> B;
    vector<int> b(B);
    rep(i, 0, B){
        cin >> b[i];
    }

    map<pair<int, int>, int> mp;
    rep(i, 0, N){
        int x = lower_bound(all(a), p[i]) - a.begin();
        int y = lower_bound(all(b), q[i]) - b.begin();
        mp[make_pair(x, y)]++;
    }
    
    int m = pow(10, 6);
    int M = 0;
    fore(i, mp){
        auto v = i.second;
        if (m > v){
            m = v;
        }
        if (M < v){
            M = v;
        }
    }
    
    ll sz = 1LL * (A + 1) * (B + 1);
    if (mp.size() < sz){
        m = 0;
    }

    cout << m << " " << M << endl;

}