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
    while i < j: # start 포인터가 end 포인터 보다 작을 때 동작
        if A[i] + A[j] == A[k]: # 찾는 값이 서로 다른 수의 합임을 체크
            if i != k and j != k: # 좋은 수 찾을 때 break해라
                result += 1
                break
            elif i == k: # 같은 수 일때는 제외
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < A[k]:
            i += 1
        else:
            j -= 1

print(result)