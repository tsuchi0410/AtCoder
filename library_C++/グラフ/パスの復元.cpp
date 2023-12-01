/*

prev[nv] : 頂点 nv はどこの v を通ってきたかを記録する配列を用意(-1 で初期化しておく)

*/

vector<long long> get_path(const vector<long long> &prev, long long t) {
  vector<long long> path;
  for (long long cur = t; cur != -1; cur = prev[cur]) {
      path.push_back(cur);
  }
  reverse(path.begin(), path.end()); // 逆順なのでひっくり返す
  return path;
}