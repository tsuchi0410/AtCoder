struct UnionFind {
  // core member
  vector<long long> par;

  // constructor
  UnionFind() { }
  UnionFind(long long n) : par(n, -1) { }
  void init(long long n) { par.assign(n, -1); }
  
  // core methods
  long long root(long long x) {
    if (par[x] < 0) return x;
    else return par[x] = root(par[x]);
  }
  
  bool same(long long x, long long y) {
    return root(x) == root(y);
  }
  
  bool merge(long long x, long long y) {
    x = root(x), y = root(y);
    if (x == y) return false;
    if (par[x] > par[y]) swap(x, y); // merge technique
    par[x] += par[y];
    par[y] = x;
    return true;
  }
  
  long long size(long long x) {
    return -par[root(x)];
  }

  map<long long, vector<long long>> groups(){
    map<long long, vector<long long>> groups;
    for (long long i = 0; i < (long long)par.size(); ++i) {
      long long r = root(i);
      groups[r].push_back(i);
    }
    return groups;
  }
  
  // debug
  friend ostream& operator << (ostream &s, UnionFind uf) {
    map<long long, vector<long long>> groups;
    for (long long i = 0; i < (long long)uf.par.size(); ++i) {
      long long r = uf.root(i);
      groups[r].push_back(i);
    }
    for (const auto &it : groups) {
      s << "group: ";
      for (auto v : it.second) s << v << " ";
      s << endl;
    }
    return s;
  }
};