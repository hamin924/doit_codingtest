# 알고 스팟 - BFS탐색
from collections import deque

n, m = map(int, input().split())

graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(m):
    graph.append(list(map(int, input())))

dist = [[-1] * n for i in range(m)] # 벽 깬 횟수 저장

def BFS(x,y):
    queue = deque()
    queue.append([x,y])
    dist[0][0] = 0 
    
    while queue:
        x, y = queue.popleft() # 현재 값 꺼내오기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or 0 > ny or ny >= n:
                continue
            if dist[nx][ny] == -1: # 아직 해당 방을 방문하지 않았을 때
                if graph[nx][ny] == 0: # 빈 공간일 때
                    dist[nx][ny] = dist[x][y] # 전에 벽 깬 횟수 그대로 전달
                    queue.appendleft([nx, ny]) # 큐의 맨 왼쪽에 넣어줌

                else: # 벽이 있다면
                    dist[nx][ny] = dist[x][y] + 1 
                    queue.append([nx, ny])
              

    

BFS(0,0)
print(dist[m-1][n-1])
