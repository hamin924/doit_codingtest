# 026 DFS와 BFS 프로그램 (백준 1260번)
from collections import deque

n, m, start = map(int,input().split())

A = [[] for _ in range(n+1)]

for i in range(m): # 리스트에 데이터 저장
    s,e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(n+1):
    A[i].sort() # 방문 노드가 여러 개일 경우, 번호가 작은 노드부터 방문하기 위해 정렬

def DFS(node):
    print(node, end=' ')
    visited[node] = True # 방문한 노드 T로 변경
    for i in A[node]: 
        if not visited[i]: 
            DFS(i)

visited = [False] * (n+1)
DFS(start)

def BFS(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    while queue: # 큐가 비어있을 때 까지
        now_node = queue.popleft()
        print(now_node, end=' ')
        for i in A[now_node]: # 현재 노드 중 미방문 노드 큐에 삽입
            if not visited[i]:
                visited[i] = True
                queue.append(i)

print()
visited = [False] * (n+1)
BFS(start)