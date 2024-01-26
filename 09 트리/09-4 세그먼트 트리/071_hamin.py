# 071 구간 합 구하기3 (백준 2042번)
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split()) # n: 수의 개수, m: 수의 변경이 일어난 횟수, k: 구간의 합을 구하는 횟수
tree_height = 0
length = n

while length != 0:
    length = length // 2
    tree_height += 1

tree_size = pow(2, tree_height+1)
leftNodeStartIndex = tree_size//2 - 1
tree = [0] * (tree_size + 1)

# 데이터를 리프 노드에 저장
for i in range(leftNodeStartIndex+1, leftNodeStartIndex + n + 1):
    tree[i] = int(input())

def setTree(i): # 인덱스 트리 생성 함수
    while i != 1:
        tree[i // 2] += tree[i]
        i -= 1

setTree(tree_size - 1) # 초기 트리 생성

def change(index, value): # 값 변경 함수
        diff = value - tree[index]
        while index > 0:
             tree[index] = tree[index] + diff
             index = index // 2

def getSum(start, end): # 구간 합 계산 함수
    partSum = 0
    while start <= end:
        if start % 2 == 1:
            partSum += tree[start]
            start += 1
        if end % 2 == 0:
            partSum += tree[end]
            end -= 1
        start = start // 2
        end = end // 2
    
    return partSum

for i in range(m+k):
    question, start, end = map(int, input().split())
    if question == 1:
        change(leftNodeStartIndex+start,end)
    elif question == 2:
        start += leftNodeStartIndex
        end += leftNodeStartIndex
        print(getSum(start, end))
    