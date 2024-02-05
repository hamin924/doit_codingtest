# 2-친구, 플로이드-워셜 알고리즘
import sys
input = sys.stdin.readline

n = int(input())
friends = [list(input()) for i in range(n)]

connected = [[0] * n for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # 2-친구인 경우
            if friends[i][j] == "Y" or (friends[i][k] == "Y" and friends[k][j] == "Y"):
                connected[i][j] = 1

result = 0
for row in connected:
    result = max(result, sum(row))

print(result)


'''
서로 친구인 경우 = 친구i에서 친구j까지 거리가 1
한 다리 건너서 아는 친구인 경우 = 친구i에서 친구j까지 거리가 2
'''