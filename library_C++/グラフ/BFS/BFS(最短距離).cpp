/*
https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_an

BFS
計算量 : O(E)

*/

int main(){
  LL(N, M);
  vector<vector<ll>> G(N);
  rep(i, M){
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

  fore(v, dist) print(v);
}