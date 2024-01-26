# 토마토 익는데 몇일 걸리는지 찾는 문제(BFS)
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0] # 왼쪽, 오른쪽
dy = [0, 0, 1, -1, 0, 0] # 위, 아래
dz = [0, 0, 0, 0, 1, -1] # 앞, 뒤

queue = deque()

def BFS():
    while queue:
        x,y,z = queue.popleft() # 현재 값 꺼내오기
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and not matrix[nx][ny][nz]:
                matrix[nx][ny][nz] = matrix[x][y][z] + 1
                queue.append([nx, ny, nz])

m, n, h = map(int, input().split()) # n -> m -> h 순서!!!
matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]


# 탐색은 입력 반대 방향
for i in range(h):
     for j in range(n):
          for k in range(m):
               if matrix[i][j][k] == 1:
                    queue.append([i,j,k])
BFS()

day = 0 # 익는데 몇일 걸리는지

for i in matrix:
     for j in i:
          if 0 in j:
               print(-1)
               exit(0)
          day = max(day, max(j))

print(day - 1)
