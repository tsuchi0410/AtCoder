ll LCM(const vl &v){
    ll x = v[0];
    if(len(v) == 1) return x;
    rep(i, 1, len(v)) x = x * v[i] / gcd(x, v[i]);
    return x;
}