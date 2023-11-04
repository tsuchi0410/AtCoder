#include <bits/stdc++.h>
using namespace std;
int MOD = 998244353;
int main(){
    int N, K;
    cin >> N >> K;
    vector<vector<int>> S;
    for (int i = 0; i < K; i++) {
        int L, R;
        cin >> L >> R;
        S.push_back({L, R});
    }
    sort(S.begin(), S.end());
    vector<long long> dp(N);
    vector<long long> dp_sum(N + 1);
    dp[0] = 1;
    dp_sum[1] = 1;
    for (int i = 1; i < N; i++) {
        for (auto& v : S) {
            int l = v[0];
            int r = v[1];
            int li = i - r;
            int ri = i - l;
            if (ri < 0) continue;
            if (li < 0) li = 0;
            dp[i] += dp_sum[ri + 1] - dp_sum[li];
            dp[i] %= MOD;
        }
        dp_sum[i + 1] = dp_sum[i] + dp[i];
    }
    cout << dp[N - 1]<< endl;
}