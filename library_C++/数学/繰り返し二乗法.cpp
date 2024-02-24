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

// a / b を MOD で割ったあまりを返す
long long division(long long a, long long b){
  return (a * pow_mod(b, MOD - 2)) % MOD;
}