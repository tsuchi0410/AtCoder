/*
計算量 : (NlogN)

vl v = {1, 3, 10, 6, 5, 5};
vl res = compress(v);

# res: [ 0 1 4 3 2 2 ]

*/


/* 1 次元 vector */
// 関数
vector<ll> compress(vl &v){
    vl vals = v;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end()); // 隣り合う重複削除
    vl res(len(v));
    for (int i = 0; i < (int)v.size(); i++) {
        res[i] = lower_bound(vals.begin(), vals.end(), v[i]) - vals.begin();
    }
    return res;
};

// lambda
lambda compress = [&](auto&& compress, vl &v) -> vl {
    vl vals = v;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end()); // 隣り合う重複削除
    vl res(len(v));
    for (int i = 0; i < (int)v.size(); i++) {
        res[i] = lower_bound(vals.begin(), vals.end(), v[i]) - vals.begin();
    }
    return res;
};


// umap で管理したいときは以下を使う
umap<ll, ll> mp;
rep(i, len(v)){
    mp[v[i]] = res[i];
}

