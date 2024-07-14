int main(){
  LL(N);
  vector<vector<vector<ll>>> G(N);
  rep(i, N - 1){
    LL(A, B, C);
    A--;
    B--;
    G[A].push_back({B, C});
    G[B].push_back({A, C});
  }
  vector<ll> dist(N, -1);
  queue<ll> q;
  dist[0] = 0;
  q.push(0);
  while(len(q)){
    ll v = q.front();
    q.pop();
    fore(nxt, G[v]){
      ll nv = nxt[0];
      ll cost = nxt[1];
      if(dist[nv] != -1){
        continue;
      }
      dist[nv] = dist[v] + cost;
      q.push(nv);
    }
  }

  ll num = *max_element(all(dist));
  ll node;
  rep(i, N){
    if(dist[i] == num){
      node = i;
    }
  }

  vector<ll> dist2(N, -1);
  queue<ll> q2;
  dist2[node] = 0;
  q2.push(node);
  while(len(q2)){
    ll v = q2.front();
    q2.pop();
    fore(nxt, G[v]){
      ll nv = nxt[0];
      ll cost = nxt[1];
      if(dist2[nv] != -1){
        continue;
      }
      dist2[nv] = dist2[v] + cost;
      q2.push(nv);
    }
  }
  ll diameter = *max_element(all(dist2));
}