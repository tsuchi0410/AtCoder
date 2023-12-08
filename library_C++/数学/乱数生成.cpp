// a 以上 b 以下のランダムな整数を返す
ll randomrange_ll(ll a, ll b){
  return a + rand() % (b - a + 1);
}

ll x = randomrange_ll(2, 10);

// a 以上 b *未満* のランダムな整数を返す
struct RandomNumberGenerator {
  mt19937 mt;

  RandomNumberGenerator() : mt(chrono::steady_clock::now().time_since_epoch().count()) {}

  int operator()(int a, int b) { // [a, b)
    uniform_int_distribution< int > dist(a, b - 1);
    return dist(mt);
  }

  int operator()(int b) { // [0, b)
    return (*this)(0, b);
  }
};

RandomNumberGenerator rng;
ll x = rng(2, 10);


