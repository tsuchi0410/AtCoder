N, M = map(int, input().split())
uf = UnionFind(N)
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    
    # 根が同じなら閉路を持つ
    if uf.root(A) == uf.root(B):
        print("No")
        exit()
    else:
        uf.unite(A, B)

print("Yes")