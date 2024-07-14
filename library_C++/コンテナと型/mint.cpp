const int MOD = 998244353;
// modint
// https://github.com/drken1215/algorithm/blob/master/MathNumberTheory/modint.cpp
template<int MOD> struct Fp {
  // inner value
  long long val;
  
  // constructor
  constexpr Fp() : val(0) { }
  constexpr Fp(long long v) : val(v % MOD) {
    if (val < 0) val += MOD;
  }
  
  // getter
  constexpr long long get() const {
    return val;
  }
  constexpr int get_mod() const {
    return MOD;
  }
  
  // comparison operators
  constexpr bool operator == (const Fp &r) const {
    return this->val == r.val;
  }
  constexpr bool operator != (const Fp &r) const {
    return this->val != r.val;
  }
  
  // arithmetic operators
  constexpr Fp& operator += (const Fp &r) {
    val += r.val;
    if (val >= MOD) val -= MOD;
    return *this;
  }
  constexpr Fp& operator -= (const Fp &r) {
    val -= r.val;
    if (val < 0) val += MOD;
    return *this;
  }
  constexpr Fp& operator *= (const Fp &r) {
    val = val * r.val % MOD;
    return *this;
  }
  constexpr Fp& operator /= (const Fp &r) {
    long long a = r.val, b = MOD, u = 1, v = 0;
    while (b) {
      long long t = a / b;
      a -= t * b, swap(a, b);
      u -= t * v, swap(u, v);
    }
    val = val * u % MOD;
    if (val < 0) val += MOD;
    return *this;
  }
  constexpr Fp operator + () const { return Fp(*this); }
  constexpr Fp operator - () const { return Fp(0) - Fp(*this); }
  constexpr Fp operator + (const Fp &r) const { return Fp(*this) += r; }
  constexpr Fp operator - (const Fp &r) const { return Fp(*this) -= r; }
  constexpr Fp operator * (const Fp &r) const { return Fp(*this) *= r; }
  constexpr Fp operator / (const Fp &r) const { return Fp(*this) /= r; }
  
  // other operators
  constexpr Fp& operator ++ () {
    ++val;
    if (val >= MOD) val -= MOD;
    return *this;
  }
  constexpr Fp& operator -- () {
    if (val == 0) val += MOD;
    --val;
    return *this;
  }
  constexpr Fp operator ++ (int) {
    Fp res = *this;
    ++*this;
    return res;
  }
  constexpr Fp operator -- (int) {
    Fp res = *this;
    --*this;
    return res;
  }
  friend constexpr istream& operator >> (istream &is, Fp<MOD> &x) {
    is >> x.val;
    x.val %= MOD;
    if (x.val < 0) x.val += MOD;
    return is;
  }
  friend constexpr ostream& operator << (ostream &os, const Fp<MOD> &x) {
    return os << x.val;
  }
  
  // other functions
  constexpr Fp pow(long long n) const {
    Fp res(1), mul(*this);
    while (n > 0) {
      if (n & 1) res *= mul;
      mul *= mul;
      n >>= 1;
    }
    return res;
  }
  constexpr Fp inv() const {
    Fp res(1), div(*this);
    return res / div;
  }
  friend constexpr Fp<MOD> pow(const Fp<MOD> &r, long long n) {
    return r.pow(n);
  }
  friend constexpr Fp<MOD> inv(const Fp<MOD> &r) {
    return r.inv();
  }
};

// Binomial coefficient
template<class mint> struct BiCoef {
  vector<mint> fact_, inv_, finv_;
  constexpr BiCoef() {}
  constexpr BiCoef(int n) : fact_(n, 1), inv_(n, 1), finv_(n, 1) {
    init(n);
  }
  constexpr void init(int n) {
    fact_.assign(n, 1), inv_.assign(n, 1), finv_.assign(n, 1);
    int MOD = fact_[0].get_mod();
    for(int i = 2; i < n; i++){
      fact_[i] = fact_[i-1] * i;
      inv_[i] = -inv_[MOD%i] * (MOD/i);
      finv_[i] = finv_[i-1] * inv_[i];
    }
  }
  constexpr mint com(int n, int k) const {
    if (n < k || n < 0 || k < 0) return 0;
    return fact_[n] * finv_[k] * finv_[n-k];
  }
  constexpr mint fact(int n) const {
    if (n < 0) return 0;
    return fact_[n];
  }
  constexpr mint inv(int n) const {
    if (n < 0) return 0;
    return inv_[n];
  }
  constexpr mint finv(int n) const {
    if (n < 0) return 0;
    return finv_[n];
  }
};

using mint = Fp<MOD>;