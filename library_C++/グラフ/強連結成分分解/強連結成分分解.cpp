// Edge Class
template<class T> struct Edge {
  int from, to;
  T val;
  Edge() : from(-1), to(-1), val(-1) { }
  Edge(int f, int t, T v = -1) : from(f), to(t), val(v) {}
  friend ostream& operator << (ostream& s, const Edge& E) {
    return s << E.from << "->" << E.to;
  }
};

// graph class
template<class T> struct Graph {
  vector<vector<Edge<T>>> list;
  vector<vector<Edge<T>>> reversed_list;
  
  Graph(int n = 0) : list(n), reversed_list(n) { }
  void init(int n = 0) {
    list.assign(n, vector<Edge<T>>());
    reversed_list.assign(n, vector<Edge<T>>());
  }
  const vector<Edge<T>> &operator [] (int i) const { return list[i]; }
  const vector<Edge<T>> &get_rev_edges(int i) const { return reversed_list[i]; }
  const size_t size() const { return list.size(); }
      
  void add_edge(int from, int to, T val = -1) {
    list[from].push_back(Edge(from, to, val));
    reversed_list[to].push_back(Edge(to, from, val));
  }
  
  void add_bidirected_edge(int from, int to, T val = -1) {
    list[from].push_back(Edge(from, to, val));
    list[to].push_back(Edge(to, from, val));
    reversed_list[from].push_back(Edge(from, to, val));
    reversed_list[to].push_back(Edge(to, from, val));
  }

  friend ostream &operator << (ostream &s, const Graph &G) {
    s << endl;
    for (int i = 0; i < G.size(); ++i) {
      s << i << " -> ";
      for (const auto &e : G[i]) s << e.to << " ";
      s << endl;
    }
    return s;
  }
};

// strongly connected components decomposition
template<class T> struct SCC {
  // input
  Graph<T> G;
  
  // results
  vector<vector<int>> scc;
  vector<int> cmp;
  Graph<T> dag;
  
  // intermediate results
  vector<bool> seen;
  vector<int> vs, rvs;
  set<pair<int,int>> new_edges;
  
  // constructor
  SCC() { }
  SCC(const Graph<T> &graph) : G(graph) { }
  void init(const Graph<T> &graph) { G = graph; }

  // dfs / rdfs
  void dfs(int v) {
    seen[v] = true;
    for (const auto &e : G[v]) if (!seen[e.to]) dfs(e.to);
    vs.push_back(v);
  }
  void rdfs(int v, int k) {
    seen[v] = true;
    cmp[v] = k;
    for (const auto &e : G.get_rev_edges(v)) if (!seen[e.to]) rdfs(e.to, k);
    rvs.push_back(v);
  }

  // reconstruct
  void reconstruct() {
    dag.init((int)scc.size());
    new_edges.clear();
    for (int i = 0; i < (int)G.size(); ++i) {
      int u = cmp[i];
      for (const auto &e : G[i]) {
        int v = cmp[e.to];
        if (u == v) continue;
        if (!new_edges.count({u, v})) {
          dag.add_edge(u, v);
          new_edges.insert({u, v});
        }
      }
    }
  }

  // main solver
  vector<vector<int>> find_scc(bool to_reconstruct = true) {
    // first dfs
    seen.assign((int)G.size(), false);
    vs.clear();
    for (int v = 0; v < (int)G.size(); ++v) if (!seen[v]) dfs(v);

    // back dfs
    int k = 0;
    scc.clear();
    seen.assign((int)G.size(), false);
    cmp.assign((int)G.size(), -1);
    for (int i = (int)G.size()-1; i >= 0; --i) {
      if (!seen[vs[i]]) {
        rvs.clear();
        rdfs(vs[i], k++);
        scc.push_back(rvs);
      }
    }

    // reconstruct DAG
    if (to_reconstruct) reconstruct();
    return scc;
  }
};

int main(){
  LL(N, M);
  Graph<ll> G(N);
  rep(i, M){
    LL(u, v);
    G.add_edge(u, v);
  }

  SCC<ll> scc_solver(G);
  const auto &scc = scc_solver.find_scc();
  
  print(len(scc));
  fore(list, scc){
    cout << len(list) << " ";
    fore(v, list){
      cout << v << " ";
    }
    cout << endl;
  }
}