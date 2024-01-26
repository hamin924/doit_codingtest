# 젤다 - 다익스트라, BFS 둘다 풀수 있음
from collections import deque
import sys

Max = sys.maxsize

def BFS(x,y, graph, cost):
    queue = deque()
    queue.append([x,y])
    
    while queue:
        x, y = queue.popleft() # 현재 값 꺼내오기
        for i in range(4): # 위,아래,왼,오른쪽 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if cost[nx][ny] > cost[x][y] + graph[nx][ny]: 
                    cost[nx][ny] = cost[x][y] + graph[nx][ny]
                    queue.append((nx, ny))

count = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    cost = [[Max] * n for i in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    cost[0][0] = graph[0][0]
    BFS(0,0,graph,cost)
    print('Problem', count, end='')
    print(":", int(cost[n-1][n-1]))
    count += 1
