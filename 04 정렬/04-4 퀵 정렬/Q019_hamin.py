# 019 k번째 수 구하기 (백준 11004번)
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

A = list(map(int, input().split()))

def quickSort(start, end, k):
        global A
        if start < end:
            pivot = partition(start, end)
            if pivot == k: # k 번째 수가 pivot이면 더 이상 구할 필요 없으므로 종료
                return
            elif k < pivot: # k가 pivot보다 작으면 왼쪽 그룹만 정렬
                quickSort(start, pivot - 1, k)
            else: # k가 pivot보다 크면 오른쪽 그룹만 정렬
                quickSort(pivot + 1, end, k)

def swap(i, j): # swap 함수 따로 빼줌
     global A
     temp = A[i]
     A[i] = A[j]
     A[j] = temp 

def partition(start, end):
    global A
    if start + 1 == end: # 데이터가 2개 인 경우 바로 비교하여 정렬
        if A[start] > A[end]:
              swap(start, end)
        return end
              
    m = (start+ end) // 2 # pivot을 중간 값으로 설정
    swap(start, m) # 처음 값, 중간 값 swap
    pivot = A[start]
    i = start + 1
    j = end

    while i <= j:
        while pivot > A[i] and i < len(A)-1: # 피벗보다 큰 수가 나올때 까지 i 증가
              i += 1
        while pivot < A[j] and j > 0: # 피벗보다 작은 수가 나올 때 까지 j 감소
                j -= 1
        if i <= j:
            swap(i,j)
            i += 1
            j -= 1

    # i==j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정
    A[start] = A[j]
    A[j] = pivot
    return j

quickSort(0, n-1, k-1)

print(A[k-1])