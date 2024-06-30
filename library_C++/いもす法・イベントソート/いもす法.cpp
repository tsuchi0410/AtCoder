int main(){
  vector<ll> imos(N + 1);
  rep(i, N){
    LL(l, r);
    l--;
    imos[l] += 1;
    imos[r] -= 1;
  }

  // 累積和
  vector<ll> s = {0};
  for(ll i = 0; i < (ll)imos.size(); i++){
    s.push_back(s[i] + imos[i])
  }
}