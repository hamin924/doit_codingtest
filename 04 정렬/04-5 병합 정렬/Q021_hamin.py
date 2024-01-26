# 021 버블 정렬 프로그램2 (백준 1517번) - 플래티넘
import sys
input = sys.stdin.readline

result = 0

def merge(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2 # divide - 배열 반으로 나누기
    left = merge(array[:mid]) # 왼쪽 값 0 ~ mid전까지
    right = merge(array[mid:]) # 오른쪽 값 mid ~ 끝까지
    
    return merge_Sort(left, right)

def merge_Sort(left, right):
    global result
    sorted = []
    index1 , index2 = 0, 0 # 나눈 배열 2개를 가리키는 인덱스

    while len(left) > index1 and len(right) > index2: 
        if left[index1] > right[index2]: # 왼쪽 값이 오른쪽 값보다 크면 더 작은값 배열에 추가
            sorted.append(right[index2])
            index2 += 1
            result += len(left) - index1 # 왼쪽에 남아있는 확인되지 않은 인덱스 만큼 더해줌
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
A = list(map(int,input().split()))
A.insert(0,0)

merge(A)

print(result)