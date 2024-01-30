# 숫자판 점프, 깊이 우선 탐색
import sys

graph = []
result = []

def DFS(x, y, num):
    if len(num) == 6:
        result.append(num)
        return
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 5 or ny <0 or ny >= 5:
            continue
        else:
            DFS(nx, ny, num + graph[nx][ny])

for i in range(5):
    graph.append(list(map(str, input().split())))

for i in range(5):
    for j in range(5):
        DFS(i, j, graph[i][j])

print(len(set(result))) # set 함수로 중복 제거