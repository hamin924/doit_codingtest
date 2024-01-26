# 074 최소 공통 조상 구하기 1 (백준 11437번) - 일반적인 방식
import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

n = int(input()) # 노드의 개수
tree = [[]for i in range(n+1)]

for i in range(0, n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0] * (n+1)
parent = [0] * (n+1)
visited = [False] * (n+1)

def BFS(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    level = 1
    now_size = 1
    count = 0
    while queue:
        now_node = queue.popleft()
        for next in tree[now_node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                parent[next] = now_node # 부모 노드 저장
                depth[next] = level # 노드 depth 저장
        count += 1
        if count == now_size: # 현재 깊이의 모든 노드를 방문
            count = 0
            now_size = len(queue)
            level += 1

BFS(1)

def LCA(a, b):
    if depth[a] < depth[b]:
        temp = a
        a = b
        b = temp

    while depth[a] != depth[b]: # 높이 맞추기
        a = parent[a]
    
    while a != b: # 공통 조상 찾기
        a = parent[a]
        b = parent[b]
    
    return a


m = int(input()) # 질의 갯수

for i in range(m):
    a,b = map(int, input().split())
    print(str(LCA(a,b)))
    print("\n")