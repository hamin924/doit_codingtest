# 008 '좋은 수' 구하기 (백준 1253번)
import sys 
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

A.sort()

result = 0


for k in range(n):
    i = 0
    j = n-1
    while i < j:
        if A[i] + A[j] == A[k]: # 찾는 값이 서로 다른 수의 합임을 체크
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < A[k]:
            i += 1
        else:
            j -= 1

print(result)