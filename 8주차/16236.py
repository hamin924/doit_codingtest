# 아기 상어 (BFS 문제)
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
result = 0
x, y, size = 0, 0, 2

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n): # 상어 위치 찾기
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j

def BFS(x,y,size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    temp = []
    while queue:
        x, y = queue.popleft() # 현재 값 꺼내오기

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] <= size: # 상어 크기보다 작으면 이동 가능
                    queue.append((nx, ny)) 
                    visited[nx][ny] = 1 # 방문 표시
                    distance[nx][ny] = distance[x][y] + 1
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))

    
    
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1])) # 역순

while True:
    shark = BFS(x, y, size) 
    if len(shark) == 0: # 아기상어가 엄마상어한테 도움을 요청함
        break

    nx, ny, dist = shark.pop()

    result += dist
    graph[x][y], graph[nx][ny] = 0,0

    x,y = nx, ny # 상어의 좌표를 먹은 물고기 좌표로 옮겨줌

    count += 1

    if count == size: # 사이즈가 같으면 이동만 가능
        size += 1
        count = 0

print(result)


'''
최단 경로
'''