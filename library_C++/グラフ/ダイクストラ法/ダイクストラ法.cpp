/*
https://algo-method.com/tasks/1008

ダイクストラ法
計算量 : O(ElogE)
概要 :
始点に最短距離 0 を設定する
まだ辿ってない点の中から最短距離が分かっていて最も距離が短い頂点に移動する
その頂点から繋がっている頂点の最短距離を設定する。この時にその頂点の最短距離を更新できるなら更新する。
これを全ての頂点の最短距離をわかるまで行う

※ 辺に負が含まれているときは使用できない -> ベルマンフォード法を使う

*/ 

int main(){
  LL(N, M);
  vector<vector<vector<ll>>> G(N);
  rep(_, M){
    LL(u, v, w);
    u--;
    v--;
    G[u].push_back({v, w});
    G[v].push_back({u, w});
  }

  vector<ll> dist(N, INF);
  dist[0] = 0;
  vector<bool> seen(N, false);

  // {cost, v}
  pqg<vector<ll>> q;
  q.push({0, 0});

  while(len(q)) {
    ll cost_v = q.top()[0];
    ll v = q.top()[1];
    q.pop();

    if(seen[v]) continue;

    seen[v] = true;
    fore(i, G[v]){
      ll nv = i[0];
      ll cost_nv = i[1];
      if(dist[nv] > cost_v + cost_nv){
        dist[nv] = cost_v + cost_nv;
        q.push({dist[nv], nv});
      }
    }
  }

  fore(i, dist) print(i);
}
