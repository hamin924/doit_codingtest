# 025 친구 관계 파악하기 (백준 13023번)
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

A = [[] for _ in range(n+1)]
visited = [False] * (n+1)
arrive = False # 도착 확인 변수

def DFS(node, depth):
    global arrive
    if depth == 5: # 깊이 5가 되면 종료
        arrive = True
        return # 함수 종료
    visited[node] = True
    for i in A[node]:
        if not visited[i]:
            DFS(i, depth+1) # 재귀함수 호출마다 깊이 증가
    visited[node] = False
    
for i in range(m):
    a, b = map(int, input().split())
    A[a].append(b) # 양방향 엣지
    A[b].append(a)

for i in range(n):
    DFS(i, 1)
    if(arrive):
        break # 반복문 종료
if arrive:
    print(1)
else:
    print(0)