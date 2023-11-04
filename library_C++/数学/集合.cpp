/*

集合演算

前提
set<ll> s1 = {1, 2, 3, 4, 5};
set<ll> s2 = {3, 4, 5, 6, 7};
set<ll> s3;

*/

// 和集合 (or)
ranges::set_union(s1, s2, inserter(s3, ranges::end(s3)));

// 積集合 (and)
ranges::set_intersection(s1, s2, inserter(s3, ranges::end(s3)));

// 差集合
// s1, s2 にすると、s1 にのみ存在する要素
// s2, s1 にすると、s2 にのみ存在する要素を返す
ranges::set_difference(s1, s2, inserter(s3, ranges::end(s3)));

// 対称差集合
// どちらか一方にのみ存在する要素を返す
ranges::set_symmetric_difference(s1, s2, inserter(s3, ranges::end(s3)));

// 部分集合判定
// s1 = {1, 2}
// s2 = {1, 2, 3} のとき
// s1 ⊂ s2 判定をしたいなら、
bool f = ranges::includes(s2, s1);

