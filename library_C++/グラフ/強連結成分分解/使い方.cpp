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