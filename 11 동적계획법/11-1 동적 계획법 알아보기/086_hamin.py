# 086 이친수 구하기 (백준 2193번)
import sys
input = sys.stdin.readline

n = int(input())

D = [[0 for j in range(2)] for i in range(n+1)]
D[1][1] = 1 # 1은 이친수
D[1][0] = 0 # 이친수는 0으로 시작하지 않으므로 한자리에서 0으로 끝나는 수는 없음

for i in range(2, n+1):
    D[i][0] = D[i-1][0] + D[i-1][1]
    D[i][1] = D[i-1][0]

print(D[n][0] + D[n][1])