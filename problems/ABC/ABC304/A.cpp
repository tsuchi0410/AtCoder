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
    vector<string> S(N);
    vector<ll> A(N);
    rep(i, 0, N){
        cin >> S[i] >> A[i];
    }
    ll P = pow(10, 10);
    int idx = 0;
    rep(i, 0, N){
        if (A[i] < P){
            P = A[i];
            idx = i;
        }
    }
    rep(i, 0, N){
        cout << S[(i + idx) % N] << endl;
    }
}