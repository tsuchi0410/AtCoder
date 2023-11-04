/*

2次元の1次元化
グリッドに辺を張るときに使う

ll H = 10;
ll W = 5;

// flatten
ll v = flatten(H, y, x);

// unflatten
ll y = unflatten[0];
ll x = unflatten[1];

*/

ll flatten(ll H, ll i, ll j){
    return i + H * j;
}

vector<ll> unflatten(ll H, ll val){
    ll y = val % H;
    ll x = val / H;
    return {y, x};
}