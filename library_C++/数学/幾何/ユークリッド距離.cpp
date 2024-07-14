long double euclid_distance(ll x1, ll y1, ll x2, ll y2) {return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));}

long long euclid_distance(long long x1, long long y1, long long x2, long long y2){
  return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
}