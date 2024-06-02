/*
出力は全部同じ
出力強度の大きさを二分探索
辺は最小全域木問題
*/


#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

#define rep(i, n) for(int i = 0; i < n ; i++)



struct UnionFind {
  // core member
  vector<int> par;

  // constructor
  UnionFind() { }
  UnionFind(int n) : par(n, -1) { }
  void init(int n) { par.assign(n, -1); }
  
  // core methods
  int root(int x) {
    if (par[x] < 0) return x;
    else return par[x] = root(par[x]);
  }
  
  bool same(int x, int y) {
    return root(x) == root(y);
  }
  
  bool merge(int x, int y) {
    x = root(x), y = root(y);
    if (x == y) return false;
    if (par[x] > par[y]) swap(x, y); // merge technique
    par[x] += par[y];
    par[y] = x;
    return true;
  }
  
  int size(int x) {
    return -par[root(x)];
  }
};

// N : 基地局
// M : 基地局を繋ぐ辺
// K : 住民

int main(){
  int N, M, K;
  cin >> N >> M >> K;
  vector<int> x(N), y(N);
  vector<int> u(M), v(M), w(M);
  vector<int> a(K), b(K);
  vector rec(N, vector<int>(N)); 
  vector<vector<int>> E;
  UnionFind uf(N);
  
  rep(i, N) cin >> x[i] >> y[i];
  rep(i, M){
    int c, d;
    cin >> c >> d >> w[i];
    u[i] = c - 1;
    v[i] = d - 1;
    E.push_back({w[i], u[i], v[i]});
  }
  sort(E.begin(), E.end());
  rep(i, K) cin >> a[i] >> b[i];
  
  rep(i, M){
    if(uf.same(E[i][1], E[i][2])){
        continue;
    }
    uf.merge(E[i][1], E[i][2]);
    rec[E[i][1]][E[i][2]] = 1;
    rec[E[i][2]][E[i][1]] = 1;
  }

  auto is_ok = [&](int P) -> bool {
    vector<int> house(K); // 使用できる家
    rep(i, N){
      rep(j, K){
        if(house[j] != 1){
          int d = (a[j] - x[i]) * (a[j] - x[i]) + (b[j] - y[i]) * (b[j] - y[i]);
          if(d <= P * P){
            house[j] = 1;
          }
        }
      }
    }
    rep(i, K){
      if(house[i] == 0){
        return false;
      }
    }
    return true;
  };

  auto bisect = [&](int ng, int ok) -> int {
    while(ok - ng > 1){
      int mid = (ok + ng) / 2;
      if(is_ok(mid)){
        ok = mid;
      }else{
        ng = mid;
      }
    }
    return ok;
  };

  int P = bisect(0, 5000);

  rep(i, N) cout << P << " ";
  cout << endl;
  rep(i, M){
    if(rec[u[i]][v[i]] == 1){
      cout << 1 << " ";
    }else{
      cout << 0 << " ";
    }
  }
  cout << endl;
}