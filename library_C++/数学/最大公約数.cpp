// 配列全体の gcd
ll GCD(const vector<ll> &v) {
    ll x = v[0];
    rep(i, len(v)) x = gcd(x, v[i]);
    return x;
}