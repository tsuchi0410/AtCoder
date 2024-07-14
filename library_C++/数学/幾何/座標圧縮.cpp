/*
計算量 : (NlogN)

vector<ll> v = {1, 3, 10, 6, 5, 5};
vector<ll> res = compress(v);

# res: [ 0 1 4 3 2 2 ]

*/


/* 1 次元 vector */
// 関数
vector<ll> compress(vector<ll> &v){
    vector<ll> vals = v;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end()); // 隣り合う重複削除
    vector<ll> res(v.size());
    for (int i = 0; i < (int)v.size(); i++) {
        res[i] = lower_bound(vals.begin(), vals.end(), v[i]) - vals.begin();
    }
    return res;
};

// lambda
lambda compress = [&](auto&& compress, vector<ll> &v) -> vector<ll> {
    vector<ll> vals = v;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end()); // 隣り合う重複削除
    vector<ll> res(v.size());
    for (int i = 0; i < (int)v.size(); i++) {
        res[i] = lower_bound(vals.begin(), vals.end(), v[i]) - vals.begin();
    }
    return res;
};


// umap で管理したいときは以下を使う
umap<ll, ll> mp;
rep(i, v.size()){
    mp[v[i]] = res[i];
}

