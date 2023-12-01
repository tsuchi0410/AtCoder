/*

計算量 : (N^3)
概要 :
3 点 (i, j, k) が同一直線上にあるかをベクトルを使って判定

*/

int main(){
  LL(N);
  VEC2(ll, X, ll, Y, N);
  rep(i, N){
    rep(j, N){
      rep(k, N){
        if(i == j or j == k or k == i){
          continue;
        }
        // 方向ベクトル(i_j)
        ll dx1 = X[j] - X[i];
        ll dy1 = Y[j] - Y[i];
        // 方向ベクトル(i_k)
        ll dx2 = X[k] - X[i];
        ll dy2 = Y[k] - Y[i];
        if(dx1 * dy2 == dx2 * dy1){
          print("Yes");
          return 0;
        }
      }
    }
  }
  print("No");
}