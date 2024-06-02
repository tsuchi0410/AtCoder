/*

nCk の組み合わせを列挙

vector<vector<long long>> comb = nCk(N, K);

*/

vector<vector<long long>> nCk(long long N, long long K){
  std::string bitmask(K, 1);
  bitmask.resize(N, 0);
  vector<vector<long long>> res;
  do{
    vector<long long> v;
    for(long long i = 0; i < N; ++i) if(bitmask[i]) v.push_back(i);
    res.push_back(v);
  }while(std::prev_permutation(bitmask.begin(), bitmask.end()));
  return res;
}