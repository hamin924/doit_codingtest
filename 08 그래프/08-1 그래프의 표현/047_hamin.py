# 047 효율적으로 해킹하기 (백준 1325번)
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n+1)]

def BFS(node):
    queqe = deque([node])
    visited = [False] * (n+1) # 방문 여부 초기화
    visited[node] = True
    count = 1
    while queqe:
        now_node = queqe.popleft()
        for i in A[now_node]:
            if not visited[i] :
                visited[i] = True
                queqe.append(i)
                count += 1
    return count

for i in range(m):
    s,e =  map(int,input().split())
    A[e].append(s) # 단방향

answer = [0 for _ in range(n+1)]

for i in range(1,n+1):
    answer[i] = BFS(i)

max_count = max(answer)

for i in range(1, n+1):
    if max_count == answer[i]:
        print(i, end=' ')