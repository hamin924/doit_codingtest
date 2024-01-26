# 029 원하는 정수 찾기 (백준 1920번)

n = int(input())

A = list(map(int, input().split()))
A.sort()

m = int(input())

target_list = list(map(int,input().split())) # 탐색할 리스트 저장


for i in range(m):
    result = False
    target = target_list[i]
    start = 0
    end = len(A)-1
    while start <= end:
        mid_index = int((start+end) / 2)
        mid_value = A[mid_index]
        if mid_value > target: # 찾는 값이 중간 값보다 작으면 왼쪽 탐색
            end = mid_index - 1
        elif mid_value < target: # 찾는 값이 중간 값보다 크면 오른쪽 탐색
            start = mid_index + 1
        else:
            result = True
            break

    if result:
        print(1)
    else:
        print(0)