<!--

verified
D - Knapsack 1
https://atcoder.jp/contests/dp/tasks/dp_d

-->
## 問題 ナップサック DP
ナップサックの重量 W 以下で価値の総和を最大化

### コード
```cpp
  LL(N, W);
  vector<ll> w(N), v(N);
  rep(i, N){
    cin >> w[i] >> v[i];
  }

  vector dp(N + 1, vector<ll>(W + 1, -1));
  dp[0][0] = 0;
  rep(i, N){
    rep(j, W + 1){
      if(dp[i][j] == -1){
        continue;
      }

      // under
      chmax(dp[i + 1][j], dp[i][j]);

      // next
      if(j + w[i] <= W){
        chmax(dp[i + 1][j + w[i]], dp[i][j] + v[i]);
      }

    }
  }

  print(max(dp[N]));

```