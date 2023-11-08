LL(N, M);
dsu uf(N);
rep(i, N){
  LL(u, v);
  if(uf.leader(u) == uf.leader(v)){
    print("cycle");
  }
  uf.merge(u, v);
}
