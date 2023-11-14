/*

ワーシャルフロイド法
計算量 : O(V^3)
概要 : 重み付き有向グラフの全ペアの最短経路問題を多項式時間で解く
*/
    

int main(){
  LL(N, M);
  vector dist(N, vector<ll>(N, INF));
  rep(i, M){
    LL(u, v, w);
    dist[u][v] = w;
  }
  
  rep(i, N){
    dist[i][i] = 0;
  }

  // k 以下の都市を通るときの全点対最短経路
  rep(k, N){
    rep(i, N){
      rep(j, N){
        chmin(dist[i][j], dist[i][k] + dist[k][j]);
      }
    }
  }

  // 負閉路判定
  rep(i, N){
    if(dist[i][i] < 0){
      print("NEGATIVE CYCLE");
      return 0;
    }
  }

}