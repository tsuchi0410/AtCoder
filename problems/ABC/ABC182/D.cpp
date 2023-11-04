#include <bits/stdc++.h>
using namespace std;
int main(){
    int N;
    cin >> N;
    vector<long long> A;
    for (int i = 0; i < N; i++) {
        int a;
        cin >> a;
        A.push_back(a);
    }
    vector<long long> S;
    S.push_back(0);
    for (int i = 0; i < N; i++) {
        S.push_back(S[i] + A[i]);
    }

    // for (auto& v : S) {
    //     cout << v << " ";
    // }
    // cout << endl;

    long long ans = 0;
    long long now = 0;
    long long rec = 0;
    for (int i = 0; i < N + 1; i++) {
        rec = max(rec, S[i]);
        ans = max(ans, now + rec);
        now += S[i];
    }
    cout << ans << endl;
}