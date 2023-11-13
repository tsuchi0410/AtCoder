string S = "Hello";

// 追加
S += "World";
S.push_back("!");

// 削除 erase(i, x) i 番目から x 文字消す
S.erase(2, 3);
S.pop_back();