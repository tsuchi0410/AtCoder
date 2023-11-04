/*

ダブリング

概要:
同じ操作を繰り返した N 回目の状態を求める
0 <= N <= 10^18 なども可

例
例えば一直線上謎すごろくで、85マス先にあるゴールにちょうど行きたいとします 。
手持ちが「1マス進む」だけのとき、自分がゴールに着くには、85ターンが必要です。
計算量は、距離を N とすると、O(N) となります。

手持ちが
 1 マス進む
 2 マス進む
 4 マス進む
 8 マス進む
 ....
 2^N マス進む

のとき、選択肢をうまいこと使えば今回の場合だと 64 + 16 + 4 + 1 の 4 回のターンでゴールへ着くことができます。
計算量は O(logN) になります。

*/

/*

verified
ABC167 D - Teleporter
https://atcoder.jp/contests/abc167/tasks/abc167_d

*/

int main(){
  LL(N, K);
  VEC(ll, A, N);

  fore(city, A){
    city--;
  }

  vvl dp(61, vl(N));
  rep(i, N){
    dp[0][i] = A[i];
  }
  rep(i, 1, 61){
    rep(j, N){
      dp[i][j] = dp[i - 1][dp[i - 1][j]];
    }
  }

  ll ans = 0;
  rrep(i, 60){
    if((1LL << i) & K){
      ans = dp[i][ans];
    }
  }

  print(ans + 1);
}