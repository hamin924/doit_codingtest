# 070 트리 순회하기 (백준 1991번)
import sys
input = sys.stdin.readline
n = int(input())
tree = {} # 딕셔너리로 선언

for i in range(n):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

def preOrder(node): # 전위 순회 : 현재 노드 -> 왼쪽 노드 -> 오른쪽 노드
    if node == ".":
        return # 자식 노드가 없는 경우
    print(node, end = '')
    preOrder(tree[node][0]) # 왼쪽 자식 노드 탐색
    preOrder(tree[node][1]) # 오른쪽 자식 노드 탐색

def inOrder(node): # 중위 순회 : 왼쪽 노드 -> 현재 노드 -> 오른쪽 노드
    if node == ".":
        return
    inOrder(tree[node][0])
    print(node, end = '')
    inOrder(tree[node][1])

def posterOrder(node): # 후위 순회 : 왼쪽 노드 -> 오른쪽 노드 -> 현재 노드 
    if node == ".":
        return
    posterOrder(tree[node][0])
    posterOrder(tree[node][1])
    print(node, end = '')

preOrder('A')
print()
inOrder('A')
print()
posterOrder('A')
print()
