# 050 집합 표현하기 (백준 1717번)
import sys
sys.setrecursionlimit(10000000) # 재귀 사용 시 시간 초과 방지
inpurt = sys.stdin.readline
n, m = map(int, input().split())

parent = [0] * (n+1)

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # 재귀 함수
        return parent[a] 

def union(a,b): # 대표 노드끼리 합치기
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
    
    
for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    question, a, b = list(map(int, input().split()))
    if question == 0: # 질의가 0이면
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    