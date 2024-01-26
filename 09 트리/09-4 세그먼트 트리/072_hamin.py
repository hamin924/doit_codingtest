# 072 최솟값 찾기2 (백준 10868번)
import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # n: 수의 개수, m: 최솟값을 구하는 횟수
tree_height = 0
length = n

while length != 0:
    length = length // 2
    tree_height += 1

tree_size = pow(2, tree_height+1)
leftNodeStartIndex = tree_size//2 - 1
tree = [sys.maxsize] * (tree_size + 1)

# 데이터를 리프 노드에 저장
for i in range(leftNodeStartIndex+1, leftNodeStartIndex + n + 1):
    tree[i] = int(input())

def setTree(i): # 인덱스 트리 생성 함수
    while i != 1:
        if tree[i // 2] > tree[i]: # 최솟값 비교
            tree[i // 2] = tree[i]
        i -= 1

setTree(tree_size - 1) # 초기 트리 생성

def getMin(start, end): # 최솟값 계산 함수 구현
    Min = sys.maxsize
    while start <= end:
        if start % 2 == 1:
            Min = min(tree[start], Min)
            start += 1
        if end % 2 == 0:
            Min = min(tree[end],Min)
            end -= 1
        start = start // 2
        end = end // 2
    
    return Min

for i in range(m):
    start, end = map(int, input().split())
    start += leftNodeStartIndex
    end += leftNodeStartIndex
    print(getMin(start, end))
    