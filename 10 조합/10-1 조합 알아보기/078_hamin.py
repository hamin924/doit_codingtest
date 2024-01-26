# 078 부녀회장이 될 테야 (백준 2775번)
import sys
input = sys.stdin.readline

D = [[0 for j in range(15)] for i in range(15)]

for i in range(1, 15):
    D[i][1] = 1 # 1호에는 항상 1명
    D[0][i] = i # 0층에는 i명

for i in range(1, 15):
    for j in range(2, 15):
        D[i][j] = D[i-1][j]+D[i][j-1]


T = int(input())

for i in range(0, T):
    k = int(input())
    n = int(input())
    print(D[k][n])
    