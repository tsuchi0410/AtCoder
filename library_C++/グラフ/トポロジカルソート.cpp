LL(N, M);
vector<vector<ll>> G(N);
vector<ld> deg(N);
rep(i, M){
  LL(u, v);
  G[u].push_back(v);
  deg[v] += 1;
}

// 入ってくる有向辺を持たないノードを列挙
queue<ll> q;
rep(v, N){  // 頂点数
  if(deg[v] == 0){
    q.push(v);
  }
}

vector<ll> lst;
while(len(q)){
  ll v = q.front();
  q.pop();
  lst.pb(v);
  fore(u, G[v]){
    deg[u] -= 1;
    if(deg[u] == 0){
      q.push(u);
    }
  }
}
