// Union-Find, we can undo
struct UnionFind {
  // core member
  vector<int> par;
  stack<pair<int,int>> history;
  
  // constructor
  UnionFind() {}
  UnionFind(int n) : par(n, -1) { }
  void init(int n) { par.assign(n, -1); }
  
  // core methods
  int root(int x) {
    if (par[x] < 0) return x;
    else return root(par[x]);
  }
  
  bool same(int x, int y) {
    return root(x) == root(y);
  }
  
  bool merge(int x, int y) {
    x = root(x), y = root(y);
    history.emplace(x, par[x]);
    history.emplace(y, par[y]);
    if (x == y) return false;
    if (par[x] > par[y]) swap(x, y);  // merge technique
    par[x] += par[y];
    par[y] = x;
    return true;
  }
  
  int size(int x) {
    return -par[root(x)];
  }

  // 1-step undo
  void undo() {
    for (int iter = 0; iter < 2; ++iter) {
      par[history.top().first] = history.top().second;
      history.pop();
    }
  }

  // erase history
  void snapshot() {
    while (!history.empty()) history.pop();
  }

  // all rollback
  void rollback() {
    while (!history.empty()) undo();
  }
  
  // debug
  friend ostream& operator << (ostream &s, UnionFind uf) {
    map<int, vector<int>> groups;
    for (int i = 0; i < uf.par.size(); ++i) {
      int r = uf.root(i);
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