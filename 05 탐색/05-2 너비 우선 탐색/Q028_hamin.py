# 028 트리의 지름 구하기 (백준 1167번)
from collections import deque

n = int(input())

A = [[] for _ in range(n+1)]

for i in range(n):
    c = list(map(int, input().split()))
    for i in range(1, len(c) - 2, 2): # 2개씩 묶어서 입력
        if c[i] != -1:
            A[c[0]].append((c[i],c[i+1]))

visited = [False] * (n+1)
distance = [0] * (n+1)

def BFS(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if not visited[i[0]]: # 노드가 방문하지 않은 노드이면
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now] + i[1] # 거리 리스트 업데이트


BFS(1)
Max = 1
for i in range(2, n+1):
    if distance[Max] < distance[i]:
        Max = i

visited = [False] * (n+1)
distance = [0] * (n+1)

BFS(Max) # max 값으로 재탐색
print(max(distance))
