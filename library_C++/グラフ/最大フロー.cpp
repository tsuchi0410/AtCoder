/*
最大フロー問題
計算量 : 総流量を F とすると、O(FE)
概要 : Ford-Fullkerson法
u -> v まで、流せるだけ流す（深さ優先探索など）

・宣言 O(N)
mf_graph<ll> G(N);

・辺の追加 O(1)
G.add_edge(u, v, w);

・辺 v の情報を取得 O(1)
mf_graph<ll>::edge i = G.get_edge(v);
debug(i.from, i.to, i.flow);

・すべての辺の情報を取得 O(E)
vector<mf_graph<ll>::edge> v = G.edges();
fore(i, v){
    debug(i.from, i.to, i.flow);
}

・流せた量を返す O(FE)
ll res = G.flow(s, t);
*/

int main(){
  LL(N, M);
  mf_graph<ll> G(N);
  rep(i, M){
    LL(u, v, w);
    u--;
    v--;
    G.add_edge(u, v, w);
  }

  ll flow = G.flow(0, N - 1);
  debug(flow)

  mf_graph<ll>::edge i = G.get_edge(0);
  debug(i.from, i.to, i.flow);

  vector<mf_graph<ll>::edge> v = G.edges();
  fore(i, v){
    debug(i.from, i.to, i.flow);
  }
}