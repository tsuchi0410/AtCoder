/*

prev[nv] : 頂点 nv はどこの v を通ってきたかを記録

*/

vector<long long> get_path(const vector<long long> &prev, long long t) {
  vector<long long> path;
  for (long long cur = t; cur != -1; cur = prev[cur]) {
      path.push_back(cur);
  }
  reverse(path.begin(), path.end()); // 逆順なのでひっくり返す
  return path;
}

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
  // prev[nv] = v : 頂点 nv は v を通って来たを記録
  vector<ll> prev(N, -1);
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
        prev[nv] = v; // 記録
        q.push({dist[nv], nv});
      }
    }
  }

  // path を復元
  rep(i, N){
    debug(i)
    debug(get_path(prev, i));
  }

}