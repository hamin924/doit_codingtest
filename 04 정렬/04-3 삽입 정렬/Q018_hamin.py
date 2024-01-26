# 018 ATM 인출 시간 계산하기  (백준 11399번)

n = int(input())

A = list(map(int, input().split()))
S = [0] * n

for i in range(1,n): # 삽입 정렬 공식
    insert_point = i
    insert_value = A[i]
    for j in range(i-1,-1, -1): # i-1에서 0까지 1감소
        if A[j] < A[i]: # 뒤에 값이 앞에 값 보다 작으면 insert point 지정
            insert_point = j +1
            break
        if j == 0:
            insert_point = 0
    
    for j in range(i, insert_point, -1): # swap 해줌
        A[j] = A[j-1]

    A[insert_point] = insert_value

S[0] = A[0]

for i in range(1, n):
    S[i] = S[i-1] + A[i] # 합 배열 저장

sum = 0

for i in range(0,n):
    sum += S[i]

print(sum)