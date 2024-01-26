# 089 연속된 정수의 합 구하기 (백준 13398번)

n = int(input())

A = list(map(int, input().split()))
L = [0] * n
L[0] = A[0]
result = L[0]

for i in range(1, n):
    L[i] = max(A[i], L[i-1] + A[i]) # 왼쪽부터 합 리스트 저장
    result = max(result, L[i]) # 수를 제거하지 않았을 때의 기본 최댓값으로 저장

R = [0] * n
R[n-1] = A[n-1]

for i in range(n-2,-1, -1):
    R[i] = max(A[i], R[i+1] + A[i]) # 오른쪽부터 합 리스트 저장

for i in range(1, n-1):
    result = max(result, L[i-1]+R[i+1])

print(result)