# 075 최소 공통 조상 구하기 2 (백준 11438번) - 플레

from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input()) # 노드의 개수
tree = [[0] for i in range(n+1)]


for i in range(0, n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0] * (n+1)
visited = [False] * (n+1)
temp = 1
kmax = 0

while temp <= n: # 최대 가능 depth 구하기
    temp <<= 1
    kmax += 1

parent = [[0 for j in range(n+1)] for i in range(kmax+1)] # parent 선언

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
                parent[0][next] = now_node # 부모 노드 저장
                depth[next] = level # 노드 depth 저장
        count += 1
        if count == now_size: # 현재 깊이의 모든 노드를 방문
            count = 0
            now_size = len(queue)
            level += 1

BFS(1)

for k in range(1, kmax+1):
    for n in range(1, n+1):
        parent[k][n] = parent[k-1][parent[k-1][n]]
        
def LCA(a, b):
    if depth[a] > depth[b]: # 더 깊은 depth가 b가 되도록
        temp = a
        a = b
        b = temp

    for k in range(kmax, -1, -1): # 깊이 빠르게 맞추기
        if pow(2,k) <= depth[b] - depth[a]:
            if depth[a] <= depth[parent[k][b]]:
                b = parent[k][b]
    
    for k in range(kmax, -1, -1): # 조상 빠르게 찾기
        if a == b: break
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
    
    LCA = a
    if a != b:
        LCA = parent[0][LCA]
    
    return LCA


m = int(input()) # 질의 갯수

for i in range(m):
    a,b = map(int, input().split())
    print(str(LCA(a,b)))
    print("\n")