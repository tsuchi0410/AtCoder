/*
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=ja

ベルマンフォード法
計算量
概要 : O(VE)
単一始点最短経路問題
負の辺が含まれているような場合でも適用可能
負の閉路がグラフに含まれている際はそれを検出することができる

*/



int main(){
  LL(N, M, r);
  vector<vector<vector<ll>>> G(N);
  rep(i, M){
    LL(u, v, w);
    G[u].push_back({v, w});
  }

  // 頂点が 1 個のときの重みの総和は 0
  if(N == 1){
    print(0);
    return 0;
  }

  lambda bellman_ford = [&](auto&& bellman_ford, ll start) -> vector<vector<ll>> {
      vector<vector<ll>> dist(2 * N, vl(N, INF)); // i 回目のステップ終了時の距離
      dist[0][start] = 0;
      // 1 回目の探索
      rep(i, 1, N){
        // 前のステップのコストを初期値とする
        rep(j, N){
          dist[i][j] = dist[i - 1][j];
        }
        rep(v, N){
          fore(k, G[v]){
            ll nv = k[0];
            ll cost = k[1];
            if(dist[i][v] == INF){
              continue;
            } 
            chmin(dist[i][nv], dist[i][v] + cost);
          }
        }
      }

      // 最後に更新がある -> 負閉路を含む
      rep(v, N){
        if(dist[N - 2][v] != dist[N - 1][v]){
          dist[N - 1][v] = -INF;
        }
      }

      // 2 回目の探索
      // -INF の部分が負閉路
      rep(i, N, 2 * N){
        rep(j, N){
          dist[i][j] = dist[i - 1][j];
        }
        rep(v, N){
          fore(k, G[v]){
            ll nv = k[0];
            ll cost = k[1];
            if(dist[i][v] == -INF){
              dist[i][nv] = -INF;
            }
          }
        }
      }

    return dist;

  };

  auto dist = bellman_ford(r);
}