int main(){
  vector<ll> imos(N + 1);
  rep(i, N){
    LL(l, r);
    l--;
    imos[l] += 1;
    imos[r] -= 1;
  }

  // 累積和
  auto s = cum(imos);

}