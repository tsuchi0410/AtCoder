int main(){
  LL(N, M);
  scc_graph G(N);
  rep(i, M){
    LL(a, b);
    G.add_edge(a, b);
  }

  auto scc = G.scc();
  debug(scc);

  print(len(scc));
  fore(vv, scc){
    cout << len(vv) << " ";
    fore(v, vv){
      cout << v << " ";
    }
    cout << endl;
  }
}