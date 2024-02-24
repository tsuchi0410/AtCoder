// グラフ、頂点数、スタート地点
vector<ll> dijkstra(vector<vector<vector<ll>>> &G, ll N, ll s){
  vector<ll> dist(N, INF);
  dist[s] = 0;
  vector<bool> seen(N, false);

  // {cost, v}
  pqg<vector<ll>> q;
  q.push({0, s});

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
  return dist;
}