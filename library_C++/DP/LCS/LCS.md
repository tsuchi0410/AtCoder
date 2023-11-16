<!--

verified
F - LCS
https://atcoder.jp/contests/dp/tasks/dp_f

-->
## 問題 LCS(最長共通部分列)
文字列 s, t が与えられます。 s の部分列かつ t の部分列であるような文字列のうち、最長のものをひとつ求めてください。

例
- axyb
- abyxb

の LCS は axb or ayb 

### コード
```cpp
  STR(S, T);
  ll N = len(S);
  ll M = len(T);
  vector dp(N + 1, vector<ll>(M + 1));
  rep(i, N){
    rep(j, M){
      if(S[i] == T[j]){
        chmax(dp[i + 1][j + 1], dp[i][j] + 1);
      }else{
        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1]);
      }
    }
  }
```

### LCS の復元
```cpp
  string ans = "";
  ll i = N;
  ll j = M;
  while(0 < i and 0 < j){
    if(dp[i][j] == dp[i - 1][j]){
      i--;
    }else if(dp[i][j] == dp[i][j - 1]){
      j--;
    }else{
      i--;
      j--;
      ans += T[j];
    }
  }
  reverse(ans);
  print(ans);
```