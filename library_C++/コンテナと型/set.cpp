// 宣言
set<int> st;
unordered_set<int> ust;

// 追加
st.insert(x);
// 削除
st.erase(x);
#define discard(s, x) {auto itr_ = s.find((x)); if (itr_ != s.end()) s.erase(itr_); }
// 所属判定 (true or false)
st.contains(x);
// 要素数
st.size();
// 空 (要素数 = 0) か (空なら true)
st.empty();

// ループ
for(auto &i : st){
}

// string -> set の変換
string s = "abc";
set<char> st(all(s));

// vector -> set の変換
vector v = {1, 1, 2, 3};
set<ll> st(all(v));


// 最小値 / 最大値 の取得 (set のみ)
auto itr = st.begin();
print(*itr);
auto itr = --st.end();
print(*itr);

// set上の二分探索
// 返り値はその値自身
// lower -> x 以上の値を返す
// upper -> x より上の値を返す
// 値が存在しないときは auto itr = st.end() を返す
auto it = st.lower_bound(x);
auto it = st.upper_bound(x);