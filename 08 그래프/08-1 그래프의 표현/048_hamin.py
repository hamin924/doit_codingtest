# 048 이분 그래프 판별하기 (백준 1707번)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
isEven = True

def DFS(node):
    global isEven
    visitied[node] = True
    for i in A[node]:
        if not visitied[i]:
            check[i] = (check[node] + 1) % 2 # 다른 집합으로 처리
            DFS(i)
        elif check[node] == check[i]: # 이미 방문한 노드가 현재 내 노드와 같은 check라면 이분 그래프 아님
            isEven = False

for i in range(n):
    v , e = map(int, input().split()) # v: 노드 개수, e: 에지 개수
    A = [[] for _ in range(v+1)]
    visitied = [False] * (v+1)
    check = [0] * (v+1)
    isEven = True

    for i in range(e):
        start, end = map(int, input().split())
        A[start].append(end)
        A[end].append(start)

    for i in range(1, v+1):
        if isEven:
            DFS(i)
        else:
            break

    if isEven:
        print("YES")
    else:
        print("NO")