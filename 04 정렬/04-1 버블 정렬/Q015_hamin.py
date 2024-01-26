# 015 수 정렬하기 1 (백준 2750번)

n = int(input())

A = [0] * n

for i in range(n): # 리스트를 엔터로 입력 받을 때
    A[i] = int(input())

for i in range(n-1): # i, j 구분 잘 해주기
    for j in range(n-1-i):
        if A[j]>A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

for i in range(n):
    print(A[i])