vector<ll> bfs(ll N, ll s, vector<vector<ll>> &G){
  vector<ll> dist(N, -1);
  queue<ll> q;
  dist[s] = 0;
  q.push(s);
  while (len(q)){
    ll v = q.front();
    q.pop();

    fore(nv, G[v]){
      if (dist[nv] != -1){
        continue;
      }
      dist[nv] = dist[v] + 1;
      q.push(nv);
    }
  }
  return dist;
}