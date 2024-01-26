# 076 이항계수 구하기 1 (백준 11050번)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

D=[[0 for j in range(n+1)] for i in range(n+1)]

for i in range(0, n+1): # 초기화
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1

for i in range(2, n+1):
    for j in range(1, i): # 고르는 수의 개수가 전체 개수를 넘을 수 없으므로 i번째까지
        D[i][j] = D[i-1][j] + D[i-1][j-1] 


print(D[n][k])

'''
조합의 연장선이 DP이다!
'''