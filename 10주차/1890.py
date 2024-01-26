# 점프, DP
import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1 # 초깃값

for i in range(n): 
    for j in range(n):
        if i == n-1 and j == n-1: # 현재 탐색하는 좌표가 오른쪽 맨 끝 점이면 break
            print(dp[i][j])
            break
        if j + graph[i][j] < n: # 오른쪽 이동
            dp[i][j+graph[i][j]] += dp[i][j]

        if i + graph[i][j] < n: # 아래로 이동
            dp[i+graph[i][j]][j] += dp[i][j]