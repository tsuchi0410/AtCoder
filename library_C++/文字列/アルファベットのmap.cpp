// 英小文字
string al = "abcdefghijklmnopqrstuvwxyz";

unordered_map<char, ll> almp;
rep(i, 26){
  almp[al[i]] = i;
}


// 英大文字
string AL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

unordered_map<char, ll> ALmp;
rep(i, 26){
  ALmp[AL[i]] = i;
}