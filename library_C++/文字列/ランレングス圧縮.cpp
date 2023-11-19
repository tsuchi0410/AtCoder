/*
ランレングス圧縮
string S = "112233334433221111";
vector<pair<char, ll>> v = encode(S);

復元
string res = decode(v);

ループ
fore(i, v){
  char c = i.first;
  ll cnt = i.second;
}
*/

vector<pair<char, ll>> encode(const string& str) {
  ll n = (ll)str.size();
  vector<pair<char, ll>> ret;
  for (ll l = 0; l < n;) {
    ll r = l + 1;
    for (; r < n && str[l] == str[r]; r++) {};
    ret.push_back({str[l], r - l});
    l = r;
  }
  return ret;
}

string decode(const vector<pair<char, ll>>& code) {
  string ret = "";
  for (auto p : code) {
    for (ll i = 0; i < p.second; i++) {
      ret.push_back(p.first);
    }
  }
  return ret;
}