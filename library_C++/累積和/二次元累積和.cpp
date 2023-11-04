/*
二次元累積和の構造体
宣言 -> add -> build -> query(左上 i, 左上 j, 右下 i, 右下 j)

// 宣言
r2d<ll> S(H, W);

// 追加
S.add(i, j, x)

// 構築
S.build();

// クエリ
S.query(i, j, i + K, j + K);

// print
S.print();

*/




template<class T>
struct r2d{
    vector<vector<T>> v;
    r2d(int H, int W) : v(H + 1, vector<T>(W + 1, 0)) {}

    void add(int x, int y, T z){
        ++x, ++y;
        if(x >= v.size() || y >= v[0].size()){
            return;
        }
        v[x][y] += z;
    }

    void build() {
        for(int i = 1; i < v.size(); i++) {
            for(int j = 1; j < v[i].size(); j++) {
                v[i][j] += v[i][j - 1] + v[i - 1][j] - v[i - 1][j - 1];
            }
        }
    }

    T query(int si, int sj, int gi, int gj) const {
        return (v[gi][gj] - v[gi][sj] - v[si][gj] + v[si][sj]);
    }

    void print(){
        for(int i = 0; i < v.size(); i++) {
            cout << "[";
            for(int j = 0; j < v[i].size(); j++) {
                if(j == v[i].size() - 1){
                    cout << v[i][j];
                }else{
                    cout << v[i][j] << ", ";
                }
            }
            cout << "]" << endl;
        }
    }
};
