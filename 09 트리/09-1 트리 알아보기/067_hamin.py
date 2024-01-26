# 067 트리의 부모 찾기 (백준 11725번)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
visited = [False] * (n+1)
tree = [[] for _ in range(n+1)] # 2차원
answer = [0] * (n+1)

for i in range(1, n):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(node):
    visited[node] = True
    for i in tree[node]:
        if not visited[i]:
            answer[i] = node # DFS를 수행하면서 부모 노드를 정담 리스트에 저장
            DFS(i)

DFS(1) # 부모 노드부터 DFS 시작

for i in range(2, n+1):
    print(answer[i])