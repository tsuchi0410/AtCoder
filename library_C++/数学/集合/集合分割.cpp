"""
計算時間はたぶんO(n!)、制約2sでn=11まで動く
分割の数はベル数になる、n=10で115975、n=11で678570

ll N = 5;
vvvl v = partition(N);
debug(v);
"""

void recursion(long long n, long long c, vector<vector<long long>> &vv, vector<vector<vector<long long>>> &vvv){
    if(c == n){
        vvv.push_back(vv);
        return;
    }
    long long m = vv.size();
    rep(i, m){
        vv[i].push_back(c);
        recursion(n, c+1, vv, vvv);
        vv[i].pop_back();
    }
    vv.push_back({c});
    recursion(n, c+1, vv, vvv);
    vv.pop_back();
    return;
}
 
vector<vector<vector<long long>>> partition(long long n){
    vector<vector<long long>> vv;
    vector<vector<vector<long long>>> vvv;
    recursion(n, 0, vv, vvv);
    return vvv;
}