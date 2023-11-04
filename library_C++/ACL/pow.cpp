// x ^ n mod(MOD)
using mint = atcoder::modint1000000007;
ll n;
mint x;
mint ans;
ans = mint(x).pow(n);

// n < 0 のときエラーを吐くので注意
ans = mint(x).pow(max(ll(0), n));