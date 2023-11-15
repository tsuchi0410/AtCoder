// 数文字判定
char c = '2';
isdigit(c);

// 英文字判定
char c = 'a';
isalpha(c)

// 英小文字判定
char c = 'a';
islower(c)

// 英大文字判定
char c = 'A';
isupper(c)

// 英小文字(char) -> 英大文字(char)
char c = 'a';
c -= 32;

// 英大文字(char) -> 英小文字(char)
char c = 'A';
c += 32;

// 英小文字(char) -> 数値（何番目か）
char c = 'a';
c -= 97; // 0

// 英小文字(char) -> 数値（何番目か）
char c = 'A';
c -= 65; // 0

// 英小文字(string) -> 英大文字(string) 
string s = "hello";
transform(s.begin(), s.end(), s.begin(), ::toupper);

// 英大文字(string) -> 英小文字(string) 
string s = "HELLO";
transform(s.begin(), s.end(), s.begin(), ::tolower);