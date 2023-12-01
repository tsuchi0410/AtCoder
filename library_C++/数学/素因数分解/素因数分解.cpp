"""
素因数分解
460 = 2^2 x 5 x 23 の場合
返り値は{{2, 2}, {5, 1}, {23, 1}}

O(√N)

ll N = 100;
auto v = prime_factorize(N);
debug(v);

mp で管理する
fore(x, v){
  mp[x[0]] += x[1];
}

"""

vector<vector<ll>> prime_factorize(ll N) {
  vector<vector<ll>> res;
  // √N まで試し割っていく
  for (ll p = 2; p * p <= N; ++p) {
    if (N % p != 0) {
      continue;
    }
    // N の素因数 p に対する指数を求める
    int e = 0;
    while (N % p == 0) {
    // 指数を 1 増やす
      ++e;
      // N を p で割る
      N /= p;
    }
    // 答えに追加
    res.push_back({p, e});
  }
  // 素数が最後に残ることがありうる
  if (N != 1) {
    res.push_back({N, 1});
  }
  return res;
}