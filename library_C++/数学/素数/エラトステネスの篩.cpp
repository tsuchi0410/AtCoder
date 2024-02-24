"""
1 以上 N 以下の整数が素数かどうかを返す
O(NloglogN)

vector<ll> ans = primes(N);
"""

vector<ll> primes(int N) {
    // テーブル
    vector<bool> isprime(N+1, true);
    // 0, 1 は予めふるい落としておく
    isprime[0] = isprime[1] = false;
    // ふるい
    for (int p = 2; p <= N; ++p) {
        // すでに合成数であるものはスキップする
        if (!isprime[p]) continue;
        // p 以外の p の倍数から素数ラベルを剥奪
        for (int q = p * 2; q <= N; q += p) {
            isprime[q] = false;
        }
    }
    vector<ll> ans;
    for(int i = 0; i <= N; i++){
        if(isprime[i] == 1) ans.push_back(i); 
    }
    return ans;
}


