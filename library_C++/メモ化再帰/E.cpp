/*

verified
https://atcoder.jp/contests/abc275/tasks/abc275_d

*/

int main(){
  LL(N);
  umap<ll, ll> mp;
  lambda f = [&](auto&& f, ll x) -> ll {
    if(x == 0){
      return 1;
    }
    if(mp.contains(x) == false){
      mp[x] = f(x / 2) + f(x / 3);
    }
    return mp[x];
  };
  print(f(N));
}