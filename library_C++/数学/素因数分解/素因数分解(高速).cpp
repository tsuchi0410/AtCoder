"""
高速素因数分解
計算量 : 前処理O(NloglogN), クエリO(logN)
概要 : エラトステネスの篩を利用して最小の素因数を記録
"""

template <typename T>
vector<T> smallest_prime_factors(T n){
  vector<T> spf(n + 1);
  for (int i = 0; i <= n; i++)
    spf[i] = i;
  for (T i = 2; i * i <= n; i++){
    // 素数だったら
    if (spf[i] == i){
      for (T j = i * i; j <= n; j += i)
      {
        // iを持つ整数かつまだ素数が決まっていないなら
        if (spf[j] == j){
          spf[j] = i;
        }
      }
    }
  }
  return spf;
}

template <typename T>
vector<T> primes(T x, vector<T> &spf){
  vector<T> ret;
  while (x != 1){
    ret.push_back(spf[x]);
    x /= spf[x];
  }
  sort(ret.begin(), ret.end());
  return ret;
}

int main()
{
  ll N = 10;
  vl v = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  ll NMAX = 1000000;
  auto spf = smallest_prime_factors(NMAX);
  rep(i, N){
    auto r = primes(v[i], spf);
    debug(r)
  }
}