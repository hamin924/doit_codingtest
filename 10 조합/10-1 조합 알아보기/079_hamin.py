# 079 다리 놓기 (백준 1010번)
import sys
input = sys.stdin.readline
D = [[0 for i in range(31)] for j in range(31)]

for i in range(0,31):
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1

for i in range(2, 31):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]

T = int(input())

for t in range(0, T):
    n, m = map(int, input().split())
    print(D[m][n])