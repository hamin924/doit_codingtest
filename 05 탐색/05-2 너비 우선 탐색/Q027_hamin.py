# 027 미로 탐색하기 (백준 2178번)
from collections import deque

dx = [0, 1, 0, -1] # 좌우를 탐색하기 위한 리스트 선언
dy = [1, 0, -1, 0] # 상하를 탐색하기 위한 리스트 선언
n, m = map(int, input().split())

A = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    num = list(input())
    for j in range(m):
        A[i][j] = int(num[j])

def BFS(i, j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    while queue:
        now_x, now_y = queue.popleft() # 현재 값 꺼내오기
        for k in range(4): # 상하좌우 탐색
            x = now_x + dx[k] # 이동 좌표
            y = now_y + dy[k]
            if x >= 0 and y >= 0 and x < n and y < m: # 이동 좌표가 범위 안에 있으면
                if A[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    A[x][y] = A[now_x][now_y] + 1
                    queue.append((x,y))


BFS(0,0)
print(A[n-1][m-1])

'''
미로 탐색 
-> BFS는 해당 깊이에서 갈 수 있는 노드 탐색을 마친 후 다음 깊이로 넘어간다
방문 했는지 노드 확인 -> 최소 이동값, visited
'''