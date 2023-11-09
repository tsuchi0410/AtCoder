/*

eg.prod(l, r).value　で値を取り出す

*/

struct S{
    long long value;
    int size;
};
using F = long long;

S op(S a, S b){ return {a.value+b.value, a.size+b.size}; }
S e(){ return {0, 0}; }
S mapping(F f, S x){ return {x.value + f*x.size, x.size}; }
F composition(F f, F g){ return f+g; }
F id(){ return 0; }

int main(){
    int N;
    std::vector<S> v(N, {0, 1});
    atcoder::lazy_segtree<S, op, e, F, mapping, composition, id> seg(v);
}