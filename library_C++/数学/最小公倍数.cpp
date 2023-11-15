long long LCM(const vector<long long> &v){
    long long x = v[0];
    if(v.size() == 1) return x;
    for(int i = 1; i < v.size(); i++) x = x * v[i] / gcd(x, v[i]);
    return x;
}