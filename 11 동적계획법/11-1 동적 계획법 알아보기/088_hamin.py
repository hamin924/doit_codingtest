# 088 계단 수 구하기 (백준 10844번)
import sys
input = sys.stdin.readline
n = int(input())
D = [[0 for j in range(11)] for i in range(n+1)] # D[자릿수][자릿수 가장 뒤에 오는 숫자]
mod = 1000000000
for i in range(1, 10): # 한자리수는 경우의 수 1가지
    D[1][i] = 1

for i in range(2, n+1):
    D[i][0] = D[i-1][1] # 가장 뒤에 오는 숫자가 0일때 그 앞에는 1만 올수 있음
    D[i][9] = D[i-1][8] # 가장 뒤에 오는 숫자가 8일때 그 앞에는 8만 올수 있음
    for j in range(1,9): # 가장 뒤에 오는 숫자가 1~8일때 그 앞에 +-1이 올수 있음
        D[i][j] = (D[i-1][j-1] + D[i-1][j+1]) % mod

sum = 0

for i in range(10):
    sum = (sum + D[n][i]) % mod


print(sum)


