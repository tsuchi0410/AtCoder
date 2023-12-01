/*　英数文字判定　*/
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


/* 英小文字・英大文字変換 */
// 英小文字(char) -> 英大文字(char)
char c = 'a';
c -= 32;

// 英大文字(char) -> 英小文字(char)
char c = 'A';
c += 32;

// 英小文字(string) -> 英大文字(string) 
string s = "hello";
transform(s.begin(), s.end(), s.begin(), ::toupper);

// 英大文字(string) -> 英小文字(string) 
string s = "HELLO";
transform(s.begin(), s.end(), s.begin(), ::tolower);


/* 英文字・数値変換 */
// 英小文字(char) -> 数値
char c = 'a';
c -= 97; // 0

// 英大文字(char) -> 数値
char c = 'A';
c -= 65; // 0

// 数値 -> 英小文字
char c = 97; // a

// 数値 -> 英大文字
char c = 65; // A


