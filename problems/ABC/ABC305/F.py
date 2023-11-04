import sys
sys.setrecursionlimit(10 ** 8)

N, M = map(int,input().split())
st = set()
st.add(1)
def dfs(v):    
    k, *us = map(int,input().split())
    for u in us:
        u = int(u)
        if not u in st:
            st.add(u)
            print(u)
            if u == N:
                input()
                exit()
            dfs(u)
            print(v)
            input()
dfs(1)