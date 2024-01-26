# 020 수 정렬하기 2 (백준 2751번)
import sys
input = sys.stdin.readline

def merge(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2 # divide - 배열 반으로 나누기
    left = merge(array[:mid]) # 왼쪽 값 0 ~ mid전까지
    right = merge(array[mid:]) # 오른쪽 값 mid ~ 끝까지
    
    return merge_Sort(left, right)

def merge_Sort(left, right):
    sorted = []
    index1 , index2 = 0, 0 # 나눈 배열 2개를 가리키는 인덱스

    while len(left) > index1 and len(right) > index2: 
        if left[index1] > right[index2]: # 왼쪽 값이 오른쪽 값보다 크면 더 작은값 배열에 추가
            sorted.append(right[index2])
            index2 += 1
        else:
            sorted.append(left[index1])
            index1 += 1
    
    while len(left) > index1 and len(right) <= index2: # 한쪽 그룹이 모두 선택된 후 남아있는 값 정리
        sorted.append(left[index1])
        index1 += 1

    while len(right) > index2 and len(left) <= index1:
        sorted.append(right[index2])
        index2 += 1
    return sorted

n = int(input())
A = []

for i in range(n): # 리스트를 엔터로 입력 받을 때
    A.append(int(input()))

result = merge(A)

for i in result:
    print(i)