/*
木の直径を O(N) で求める
任意の頂点 s を選ぶ
s から DFS/BFS によって、最も遠くにある頂点 u を探索する
u から DFS/BFS によって、最も遠くにある頂点 v を探索する
u と v を結ぶパスが直径となる
*/


int main(){
  LL(N);
  vector<vector<ll>> G(N);
  rep(i, N - 1){
    LL(u, v);
    u--;
    v--;
    G[u].push_back(v);
    G[v].push_back(u);
  }

  vector<ll> dist(N, -1);
  queue<ll> q;
  dist[0] = 0;
  q.push(0);
  while(len(q)){
    ll v = q.front();
    q.pop();
    fore(nv, G[v]){
      if(dist[nv] != -1){
        continue;
      }
      dist[nv] = dist[v] + 1;
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
    fore(nv, G[v]){
      if(dist2[nv] != -1){
        continue;
      }
      dist2[nv] = dist2[v] + 1;
      q2.push(nv);
    }
  }
  ll diameter = *max_element(all(dist2));
}
