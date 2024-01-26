# 046 특정 거리의 도시 찾기 (백준 18352번)
from collections import deque
import sys
input = sys.stdin.readline # 반복문으로 input 입력 받을 때 시간 초과 안뜨기 위해

n, m, k, x = map(int, input().split())
A = [[] for _ in range(n+1)]
answer = []
visited = [-1] * (n+1) # -1로 초기화

def BFS(node):
    queue = deque()
    queue.append(node)
    visited[node] += 1
    while queue: # 큐가 비어있을 때 까지
        now_node = queue.popleft()
        for i in A[now_node]: # 현재 노드 중 미방문 노드 큐에 삽입
            if visited[i] == -1:
                visited[i] = visited[now_node]+ 1
                queue.append(i)

for i in range(m): # 인접 리스트로 데이터 저장
    s,e = map(int, input().split())
    A[s].append(e)

BFS(x)

for i in range(n+1):
    if visited[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)