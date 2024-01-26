# 최단 거리 문제(BFS)
from collections import deque

n, m = map(int, input().split())
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(n):
    graph.append(list(map(int, input())))

def BFS(x,y):
    # 벽 파괴 가능 여부를 담은 visited
    visited = [[[0 for _ in range(2)] for j in range(m) for i in range(n)]]
    visited[x][y][0] = 1
    queue = deque()
    queue.append((x,y,0))
    
    while queue:
        x, y, c = queue.popleft() # 현재 값 꺼내오기
        if (x,y) == (n-1,m-1): # 도착했을 때
            return visited[x][y][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or 0 > ny or ny >= m:
                continue
            if graph[nx][ny] == 1 and c == 0 and not visited[nx][ny][1]: # 벽 한번도 안부수고, 다음 이동할 곳이 벽일때
                queue.append((nx, ny, 1)) # 벽 부순 상태 1로 표현
                visited[nx][ny][1] = visited[x][y][0] + 1

            elif graph[nx][ny] == 0 and not visited[nx][ny][c]: # 벽이 아닐 때
                queue.append((nx, ny, c))
                visited[nx][ny][c] = visited[x][y][c] + 1 # 이전 경로 + 1
        return 0

result = BFS(0,0)
if result:
    print(result)
else:
    print(-1)

