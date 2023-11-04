import sys

A = list(map(int,input().split()))

N = A[0]
Y = A[1]

for yukiti in range(0, N+1):
    for higuti in range(0, N-yukiti+1):
        noguti = N - yukiti - higuti
        if yukiti*10000 + higuti*5000 + noguti*1000 == Y:
            print(yukiti, higuti, noguti)
            sys.exit()
            

print("-1 -1 -1")
    