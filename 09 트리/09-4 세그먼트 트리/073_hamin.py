# 073 구간 곱 구하기 (백준 11505번)
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split()) # n: 수의 개수, m: 수의 변경이 일어난 횟수, k: 구간의 합을 구하는 횟수
tree_height = 0
length = n
mod = 1000000007

while length != 0:
    length = length // 2
    tree_height += 1

tree_size = pow(2, tree_height+1)
leftNodeStartIndex = tree_size//2 - 1
tree = [1] * (tree_size + 1) # 곱셈이므로 초깃값 1로 저장

# 데이터를 리프 노드에 저장
for i in range(leftNodeStartIndex+1, leftNodeStartIndex + n + 1):
    tree[i] = int(input())

def setTree(i): # 인덱스 트리 생성 함수
    while i != 1:
        tree[i // 2] = tree[i//2] * tree[i] % mod
        i -= 1

setTree(tree_size - 1) # 초기 트리 생성

def change(index, value): # 값 변경 함수
        tree[index] = value
        while index > 1:
             index = index // 2
             tree[index] = tree[index * 2] %mod * tree[index * 2 +1] % mod
             

def getMul(start, end): # 구간 합 계산 함수
    partMul = 1
    while start <= end:
        if start % 2 == 1:
            partMul = partMul * tree[start] % mod
            start += 1
        if end % 2 == 0:
            partMul = partMul * tree[end] % mod
            end -= 1
        start = start // 2
        end = end // 2
    
    return partMul

for i in range(m+k):
    question, start, end = map(int, input().split())
    if question == 1:
        change(leftNodeStartIndex+start,end)
    elif question == 2:
        start += leftNodeStartIndex
        end += leftNodeStartIndex
        print(getMul(start, end))
    