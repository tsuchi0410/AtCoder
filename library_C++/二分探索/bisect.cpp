// set
template <typename T>
T set_bisect_left(set<T> &X, T v){
  auto itr = X.lower_bound(v);
  T obj = *itr;
  return obj;
}
template <typename T>
T set_bisect_right(set<T> &X, T v){
  auto itr = X.upper_bound(v);
  T obj = *itr;
  return obj;
}
// multiset
template <typename T>
T mset_bisect_left(mset<T> &X, T v){
  auto itr = X.lower_bound(v);
  T obj = *itr;
  return obj;
}
template <typename T>
T mset_bisect_right(mset<T> &X, T v){
  auto itr = X.upper_bound(v);
  T obj = *itr;
  return obj;
}
// map
template <typename T, typename U>
pair<T, U> map_bisect_left(map<T, U> &X, T v){
  auto itr = X.lower_bound(v);
  pair<T, U> obj = *itr;
  return obj;
}
template <typename T, typename U>
pair<T, U> map_bisect_right(map<T, U> &X, T v){
  auto itr = X.upper_bound(v);
  pair<T, U> obj = *itr;
  return obj;
}