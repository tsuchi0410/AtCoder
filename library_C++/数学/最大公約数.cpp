// 配列全体の gcd
ll GCD(const vl &v) {
    ll x = v[0];
    rep(i, len(v)) x = gcd(x, v[i]);
    return x;
}