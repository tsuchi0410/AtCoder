// (x ^ n) % MOD

long long pow_mod(long long x, long long n) {
  long long ret = 1;
  while (n > 0) {
    if (n & 1) ret = ret * x % MOD;
    x = x * x % MOD;
    n >>= 1;
  }
  return ret;
}

long long nCr_mod(long long n, long long r) {
  long long x = 1, y = 1;
  for (int i = 0; i < r; i++) {
    x = x * (n - i) % MOD ;
    y = y * (i + 1) % MOD;
  }
  return x * pow_mod(y, MOD - 2) % MOD;
}

// mint
mint pow_mod(mint x, ll n) {
  mint ret = 1;
  while (n > 0) {
    if (n & 1) ret *= x;
    x *= x;
    n >>= 1;
  }
  return ret;
}

// a / b を MOD で割ったあまりを返す
long long division(long long a, long long b){
  return (a * pow_mod(b, MOD - 2)) % MOD;
}