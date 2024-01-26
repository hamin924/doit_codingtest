# 068 리프 노드의 개수 구하기 (백준 1068번)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n)]
visited = [False] * (n)
answer = 0
p = list(map(int, input().split()))

for i in range(n):
    if p[i] != -1: # 루트 노드가 아니면
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i

def DFS(node):
    global answer
    visited[node] = True
    cNode = 0 # 자식 노드 갯수
    for i in tree[node]:
        if not visited[i] and i != deleteNode: # 삭제 노드일때 탐색 중지
           cNode += 1
           DFS(i)
    if cNode == 0:
        answer += 1 # 자식 노드 수가 0개일때 리프 노드로 간주하고 정답 값 증가

deleteNode = int(input())

if deleteNode == root:
    print(0)
else:
    DFS(root)
    print(answer)
