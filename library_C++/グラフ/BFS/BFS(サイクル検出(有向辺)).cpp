/*
https://algo-method.com/tasks/971

計算量 : O(V + E)
概要 : BFS でトポロジカルソートしたとき、適切にできなかったらサイクルが存在する
*/

int main(){
  LL(N, M);
  vector<vector<ll>> G(N);
  rep(i, M){
    LL(v, u);
    G[u].push_back(v);
  }

  vl order; // トポロジカルソートの結果を格納

  vector<ll> ind(N); // indegree : 入次数
  rep(v, N){
    fore(u, G[v]){
      ind[u]++;
    }
  }

  queue<ll> q;
  // 入次数 = 0 の頂点から探索
  rep(v, N){
    if (ind[v] == 0){
      q.push(v);
    }
  }
  while (len(q)){
    ll v = q.front();
    q.pop();

    order.pb(v); // トポロジカルソートの結果を追加

    fore(nv, G[v]){
      ind[nv]--; // v -> nv から、v を削除するので入次数を 1 減らす
      if (ind[nv] == 0){
        q.push(nv);
      }
    }
  }

  if (len(order) == N){
    print("Yes");
  }else{
    print("No");
  }
}