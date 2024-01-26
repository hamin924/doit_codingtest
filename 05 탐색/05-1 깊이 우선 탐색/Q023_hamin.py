# 023 연결 요소의 개수 구하기 (백준 1517번)
import sys
sys.setrecursionlimit(10**6) # 재귀 최대 깊이 설정
input = sys.stdin.readline

n, m = map(int, input().split())

A = [[] for _ in range(n+1)]

visited = [False] * (n+1)
count = 0 # 연결 요수 개수

def DFS(node):
    visited[node] = True # 방문한 노드 T로 변경
    for i in A[node]:
        if not visited[i]:
            DFS(i)

for i in range(m):
    u, v = map(int, input().split())
    A[u].append(v) # 방향이 없으므로 양쪽에 edge 더하기
    A[v].append(u)

for i in range(1, n+1):
    if not visited[i]: # 현재 노드 중 방문하지 않았던 노드만 탐색
        count += 1
        DFS(i)

print(count)

'''
파이썬의 재귀 최대 깊이의 기본설정이 1,000회 이므로 10**6으로 바꿔줌
'''