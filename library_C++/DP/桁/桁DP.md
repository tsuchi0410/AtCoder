## 桁 DP の基本
### 桁 DP が適用できる問題
- N が非常に大きく64bitで収まらない
- 「 0 以上 N 以下の整数」について条件に合うものを数える

### dp の定義
- dp[i][flag][j]
- i 桁目まで見て、今見ている桁を x とすると
  - flag == false のとき
    - x -> x
    - x -> x 未満
  - flag == true のとき
    - 0 ~ 9 -> 0 ~ 9
- の遷移を考える
- 初期値は dp[0][0][0] = 1

## 問題 0 でない個数を数える
E - Almost Everywhere Zero
https://atcoder.jp/contests/abc154/tasks/abc154_e
---
1 以上 N 以下の整数であって、10 進法で表したときに、0 でない数字がちょうど K 個あるようなものの個数を求めてください。

主な制約
- 1 ≤ N ≤ 10^100
- 1 ≤ K ≤ 3

### 解法
dp[i][flag][j] として、j は 0 でない数字の個数を管理

### コード
```cpp
int main(){
  STR(N);
  LL(K);
  vector dp(len(N) + 1, vector(2, vector<ll>(K + 2))); // dp[i][flag][j] 
  dp[0][0][0] = 1;
  rep(i, len(N)){
    ll num = ctoll(N[i]); // i 桁目の数字
    rep(flag, 2){
      rep(j, K + 1){
        if(flag == 0){ // N からの遷移
          if(num == 0){
            dp[i + 1][0][j] += dp[i][0][j];
          }else{
            rep(k, num + 1){
              if(k == 0){
                dp[i + 1][1][j] += dp[i][0][j];
              }else if(k == num){
                dp[i + 1][0][j + 1] += dp[i][0][j];
              }else{
                dp[i + 1][1][j + 1] += dp[i][0][j];
              }
            }
          }
        }else{
          dp[i + 1][1][j] += dp[i][1][j];
          dp[i + 1][1][j + 1] += dp[i][1][j] * 9;
        }
      }
    }
  }
  print(dp[len(N)][0][K] + dp[len(N)][1][K]);
}
```

***

<br>


