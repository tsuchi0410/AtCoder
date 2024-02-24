// https://atcoder.jp/contests/abc340/tasks/abc340_c

int main(){
  LL(N);
  unordered_map<ll, ll> mp;
  lambda f = [&](auto&& f, ll x) -> ll {
    if(x == 1){
      return 0;
    }
    if(mp.contains(x)){
      return mp[x];
    }
    mp[x] = f(x / 2) + f((x + 1) / 2) + x;
    return mp[x];
  };
  print(f(N));
}