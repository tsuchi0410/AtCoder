int main(){
  LL(N);
  VEC(ll, A, N);

  // 双方向 map を作成
  // -1(head) <-> A0 <-> A1 <-> ... <-> -1(tail)
  map<ll, ll> nxt, prev;
  rep(i, N - 1){
    nxt[A[i]] = A[i + 1];
    prev[A[i + 1]] = A[i];
  }
  nxt[A[N - 1]] = -1;
  prev[A[0]] = -1;

  LL(Q);
  rep(_, Q){
    LL(op);
    if(op == 1){
      // 要素 x の後ろに 要素 y を挿入
      LL(x, y);
      prev[y] = x;
      nxt[y] = nxt[x];
      if(nxt[x] != -1){
        prev[nxt[x]] = y;      
      }
      nxt[x] = y;
    }else{
      // 要素 x を削除
      LL(x);
      if(prev[x] != -1){
        nxt[prev[x]] = nxt[x];
      }
      if(nxt[x] != -1){
        prev[nxt[x]] = prev[x];
      }
      prev.erase(x);
      nxt.erase(x);
    }
  }
  
  ll first;
  fore(node, prev_node, prev){
    if(prev_node == -1){
      first = node;
    }
  }

  ll node = first;
  while(node != -1){
    cout << node << " ";
    node = nxt[node];
  }
  cout << endl;

}