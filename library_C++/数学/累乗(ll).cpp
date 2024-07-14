ll powll(ll n, ll r){
  if (r == 0) return 1;
  else if (r % 2 == 0) return powll(n * n, (ll)(r / 2));
  else return n * powll(n, r - 1);
}